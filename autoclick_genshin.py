import pynput
import keyboard
from pynput.keyboard import Key,  Controller

keyboard = controller()

Press = False
while True:
    Press = False
    if keyboard.is_pressed("Key.f8"):
        Press = True

    while Press = True:
        keyboard.press('f')
        if keyboard.is_pressed('Key.f8'):
            Press = False


