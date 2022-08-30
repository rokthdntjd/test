import pynput
import keyboard
from pynput.keyboard import Key, Controller
keyboard = Controller()

if keyboard.is_pressed('a'):
    keyboard.press('f')
    keyboard.release('f')