from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices
import logging
import sys

# configure logging to write password generation history
logging.basicConfig(filename="generation.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%dT%H:%M:%S")

# define available character sets and their default states
charset_options = {
    "-m": {"enabled": True, "charset": ascii_uppercase + ascii_lowercase, "help": "uppercase & lowercase letters (default)"},
    "-u": {"enabled": False, "charset": ascii_uppercase, "help": "uppercase letters only"},
    "-l": {"enabled": False, "charset": ascii_lowercase, "help": "lowercase letters only"},
    "-n": {"enabled": True, "charset": digits, "help": "digits"},
    "-s": {"enabled": True, "charset": punctuation, "help": "symbols"},
}

# flags that cannot be used together
MUTUALLY_EXCLUSIVE_FLAGS = {"-m", "-u", "-l"}
ENABLE_LOGGING = True

# error messages
MUTUALLY_EXCLUSIVE_ERROR_MESSAGE = "error: options -m, -u and -l are mutually exclusive. please select only one of them."
INVALID_COMMAND_ERROR_MESSAGE = "error: invalid command usage. please run `main.py --help` for detailed instructions."
UNKNOW_FLAG_ERROR_MESSAGE = "error: unknown option. run main.py --help to view all available flags."

# parse command-line arguments
parsed_args = sys.argv[1:]

# default password length
length = 10

# password result container
password = {
    "available": False,
    "value": None,
}


# log password generation to file
def log_password_generation(flags, length, password):
    flags_str = ",".join(flags) if flags else "default"
    logging.info(f"flags: [{flags_str}] | length: {length} | {password}")


# validate that only one of -m, -u, -l is used
def validate_flag_combination(flags):
    count = sum(1 for flag in flags if flag in MUTUALLY_EXCLUSIVE_FLAGS)
    result = "VALID"
    if count > 1:
        result = "MUTUALLY_EXCLUSIVE"
    return result


# display help guide if requested
def guide(flags: list) -> str:
    result = ""
    if flags == ["--help"]:
        print("\noptions guide:\n")
        for key, value in charset_options.items():
            result += "\t" + key + ": " + value["help"]
    return result


# main logic for parsing flags and generating password
def main(flags: list) -> dict:
    global length
    validation = True
    tokens = dict()

    # parse flags and values
    for flag in flags.copy():
        if flag.isdigit():
            length = int(flag)
            flags.remove(flag)
        elif ":" in flag:
            key, value = flag.split(":", 1)
            tokens[key] = value
            flags.remove(flag)
            flags.append(key)
        else:
            validation = "INVALID_COMMAND"
            break

    # validate flag keys
    if set(tokens.keys()).issubset(set(charset_options.keys())):
        for token in tokens:
            charset_options[token]["enabled"] = True if tokens[token] == "yes" else False
        validation = validate_flag_combination(tokens.keys())
    else:
        validation = "UNKNOWN_FLAG"

    # re-check validation if still marked True
    if validation == True:
        validation = validate_flag_combination(tokens.keys())

    # handle validation outcomes
    match validation:
        case "INVALID_COMMAND":
            password["value"] = INVALID_COMMAND_ERROR_MESSAGE
        case "UNKNOWN_FLAG":
            password["value"] = UNKNOW_FLAG_ERROR_MESSAGE
        case "MUTUALLY_EXCLUSIVE":
            password["value"] = MUTUALLY_EXCLUSIVE_ERROR_MESSAGE
        case "VALID":
            # disable -m if -u or -l is explicitly enabled
            for token in tokens:
                if token in {"-u", "-l"}:
                    charset_options["-m"]["enabled"] = False
            # build character pool and generate password
            available_chars = "".join(cfg["charset"] for cfg in charset_options.values() if cfg["enabled"])
            password["available"] = True
            password["value"] = "".join(choices(available_chars, k=length))

    return password


# entry point
if __name__ == "__main__":
    result = guide(parsed_args)
    if result:
        print(result)
        exit_status = 0
    else:
        result = main(parsed_args)
        if password["available"]:
            if ENABLE_LOGGING:
                log_password_generation(parsed_args, length, password["value"])
            exit_status = 0
        else:
            exit_status = 1
        print("\n" + password["value"])
        sys.exit(exit_status)
