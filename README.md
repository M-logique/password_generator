<h1>🔐 password_generator – Advanced Command-Line Password Generator</h1>

<p>
    <strong>password_generator</strong> is a flexible and secure Python-based password generator designed for quick
    command-line usage.
    It supports multiple character set options, customizable length, and detailed logging of generated passwords for
    auditing or debugging purposes.
</p>

<hr>

<h2>📂 Project Files</h2>
<ul>
    <li><code>passgen.py</code> – Main Python script for password generation.</li>
    <li><code>generation.log</code> – Log file storing password generation history (timestamp, flags, length, and
        generated password).</li>
</ul>

<hr>

<h2>⚙️ Features</h2>
<ul>
    <li>Generate strong passwords with customizable character sets.</li>
    <li>Supports uppercase, lowercase, digits, and symbols.</li>
    <li>Mutually exclusive flag validation to prevent conflicting options.</li>
    <li>Customizable password length via command-line arguments.</li>
    <li>Detailed logging of each generation event.</li>
    <li>Built-in <code>--help</code> guide for quick reference.</li>
</ul>

<hr>

<h2>📦 Requirements</h2>
<ul>
    <li>Python 3.7+</li>
    <li>No external dependencies (uses only Python standard library).</li>
</ul>

<hr>

<h2>🚀 Usage</h2>

<pre><code>python passgen.py [options] [length]
</code></pre>

<p><strong>Examples:</strong></p>
<ul>
    <li><code>python passgen.py</code> → Generates a 10-character password using default sets (letters, digits,
        symbols).</li>
    <li><code>python passgen.py 16</code> → Generates a 16-character password with default sets.</li>
    <li><code>python passgen.py -u:yes -n:no 12</code> → Generates a 12-character password with uppercase letters only
        (no digits).</li>
    <li><code>python passgen.py --help</code> → Displays the options guide.</li>
</ul>

<hr>

<h2>🏷️ Available Flags</h2>

<table>
    <thead>
        <tr>
            <th>Flag</th>
            <th>Description</th>
            <th>Default State</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>-m</code></td>
            <td>Uppercase &amp; lowercase letters</td>
            <td>Enabled</td>
        </tr>
        <tr>
            <td><code>-u</code></td>
            <td>Uppercase letters only</td>
            <td>Disabled</td>
        </tr>
        <tr>
            <td><code>-l</code></td>
            <td>Lowercase letters only</td>
            <td>Disabled</td>
        </tr>
        <tr>
            <td><code>-n</code></td>
            <td>Digits (0-9)</td>
            <td>Enabled</td>
        </tr>
        <tr>
            <td><code>-s</code></td>
            <td>Symbols (punctuation)</td>
            <td>Enabled</td>
        </tr>
    </tbody>
</table>

<p>
    <strong>Note:</strong> <code>-m</code>, <code>-u</code>, and <code>-l</code> are <em>mutually exclusive</em>. Only
    one can be active at a time.
    If you disable <code>-m</code> and do not enable <code>-u</code> or <code>-l</code>, no letters will be included in
    the generated password — it will only contain digits and/or symbols based on other enabled options.
</p>

<hr>

<h2>🛡️ Validation Rules</h2>
<ul>
    <li>Only one of <code>-m</code>, <code>-u</code>, or <code>-l</code> can be enabled at once.</li>
    <li>Unknown flags trigger an error message.</li>
    <li>Invalid command syntax returns a usage error.</li>
</ul>

<hr>

<h2>📝 Logging</h2>
<p>
    If logging is enabled (<code>ENABLE_LOGGING = True</code>), each generated password is recorded in
    <code>generation.log</code> with:
</p>
<ul>
    <li>Timestamp</li>
    <li>Enabled flags</li>
    <li>Password length</li>
    <li>Generated password</li>
</ul>

<pre><code>2025-09-19T20:15:42 INFO: flags: [-m,-n,-s] | length: 12 | aB3$kP!x9Q@r
</code></pre>

<hr>

<h2>📖 Help Menu</h2>
<p>Run the following command to see available options:</p>
<pre><code>python passgen.py --help
</code></pre>

<hr>

<h2>🔍 How It Works</h2>
<ol>
    <li>Parses command-line arguments for flags and password length.</li>
    <li>Validates that only one of the mutually exclusive flags is active.</li>
    <li>Builds a character pool based on enabled options.</li>
    <li>Generates a random password using <code>random.choices()</code>.</li>
    <li>Logs the result if logging is enabled.</li>
</ol>

<hr>

<h2>💡 Tip for Faster Access</h2>
<p>
    For quicker usage, place <code>passgen.py</code> inside a folder that your terminal opens by default (e.g., your
    home directory) or add its folder path to your system's <code>PATH</code> environment variable.
    This way, you can run <code>passgen.py</code> from anywhere without navigating to its directory first.
</p>