from pynput.mouse import Controller, Button
import keyboard
import time
def t():
    mouse = Controller()
    for j in range(200):
        for i in range(6):
            mouse.click(Button.left)
            time.sleep(0.1)
        time.sleep(0.2)
        #mouse.position = (600, 265)
        mouse.position = (670, 265)
        time.sleep(0.1)
        mouse.click(Button.left)
        #time.sleep(0.35)
        time.sleep(10)
keyboard.add_hotkey('ctrl+alt', t)
keyboard.wait('ctrl+c')