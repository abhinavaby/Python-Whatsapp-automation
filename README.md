
<!DOCTYPE html>
<html lang="en">
<body>

  <h1 align="center">📱 WhatsApp Message Scheduler</h1>

  <p align="center">
        A Python-based automation tool that schedules and sends WhatsApp messages using the 
        <a href="https://www.twilio.com">Twilio WhatsApp API</a>.
    </p>

  <hr>

   <h2>🚀 Features</h2>
    <ul>
        <li><b>Future Scheduling:</b> Input a specific date and time for message delivery.</li>
        <li><b>Automated Delay:</b> Calculates precise wait times using Python's <code>datetime</code> and <code>time</code> modules.</li>
        <li><b>Simple CLI:</b> Interactive command-line interface for easy user input.</li>
    </ul>

  <h2>🛠️ Setup & Installation</h2>
    <p>Before running the script, ensure you have the following:</p>
    <ol>
        <li>
            <b>Twilio Account:</b> Sign up at <a href="https://www.twilio.com">Twilio.com</a> and get your Account SID and Auth Token.
        </li>
        <li>
            <b>Install Dependencies:</b>
            <pre><code>pip install twilio</code></pre>
        </li>
    </ol>
    <h2>📝 How to Use</h2>
    <ol>
        <li>Replace the <code>account_sid</code> and <code>auth_token</code> in the script with your credentials.</li>
        <li>Run the script: <code>python main.py</code></li>
        <li>Enter the recipient's name, number (with country code), and message body.</li>
        <li>Provide the scheduled date (<code>YYYY-MM-DD</code>) and time (<code>HH:MM</code>).</li>
    </ol>

  <h2>⚠️ Security Note</h2>
    <p>
    Do <b>not</b> hardcode your API keys in public repositories. It is best practice to use 
        <a href="https://docs.python.org">environment variables</a> 
        or a <code>.env</code> file to keep your credentials secure.
    </p>

  <hr>
    <p align="center">
        Made with ❤️ for Automation
    </p>

</body>
</html>
