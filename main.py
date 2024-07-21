import os
import keyboard

VERSION = "alpha 0.0.1"


print("\t\tWelcome to the Win Cleaner!")

while kybrd != "q":
    kybrd = keyboard.hook()

    if kybrd == "Ctrl + v":
        print(f"version: {VERSION}")