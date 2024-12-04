KeyLogger Python Script :

This repository contains a simple Python-based keylogger implementation that captures keystrokes from specified target applications. It logs keystrokes, identifies sensitive information such as usernames, emails, and passwords, and writes them to a log file.

Features :

Keystroke Logging: Captures all keypresses, including special keys such as Backspace, Enter, and Tab.
Sensitive Data Detection: Detects potential usernames, emails, and passwords based on user input.
Application-Specific Logging: Tracks keystrokes in specific applications (e.g., Terminal, Gedit, Firefox).
Active Window Monitoring: Logs the active window when it changes and associates keystrokes with the correct window.
Log File: All captured data is written to a log file (log.txt).


Requirements :

Python 3.x
pynput library for capturing keyboard events.
xdotool for identifying the active window (Linux-only).
Install Dependencies
You can install the required dependencies using pip:

bash code :
pip install pynput
For xdotool, you can install it on Linux using:

bash code :
sudo apt-get install xdotool


Usage :
Clone or download the repository.
Customize the target_apps list to include the applications you want to monitor.


Run the script.

Example
python
Copy code
target_apps = ["Terminal", "Gedit", "Firefox"]  # Specify target applications
keylogger = KeyLogger(target_apps)
keylogger.start()  # Start logging keystrokes


Features in Detail :

Logging Keystrokes: The script logs every keypress, including regular characters and special keys like Backspace, Enter, and Tab.
Sensitive Data Capture: The script attempts to detect usernames, emails, and passwords based on common patterns in the captured text.
Window Switching Detection: If the active window changes, it logs the new window and resets the input buffer.
Target Application Filtering: You can specify which applications to track. For example, it might be set to only track "Terminal", "Firefox", and "Gedit".
Log File
All the captured data is written to log.txt. It contains:

Captured usernames and passwords (with passwords masked).
Log of keystrokes, including special keys (e.g., Enter, Backspace).
Information on window changes.
Example log entries:

yaml code : 
Keylogger Started.
[Switched to: Terminal]
Captured Username/Email: user123
Captured Password: ********
[Switched to: Firefox]


Disclaimer : 
This code is for educational purposes only. Using this script to capture keystrokes or monitor applications without the user's consent may be illegal and unethical. Always ensure that you have proper permission before using or deploying this script.
