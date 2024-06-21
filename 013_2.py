import keyboard
import time

def listener_1():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('inc')
    print('inc')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+1', listener_1)

def listener_2():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('gg')
    print('gg')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+2', listener_2)

def listener_3():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('just wait a minute pls,i need ten diams to finsish a challenge')
    print('just wait a minute pls,i need ten diams to finsish a challenge')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+3', listener_3)

def listener_4():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('anyone def?')
    print('anyone def?')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+4', listener_4)

def listener_5():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('anyone build?')
    print('anyone build?')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+5', listener_5)

def listener_6():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('im not good at it')
    print('im not good at it')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+6', listener_6)

def listener_7():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('i need iron plssss')
    print('i need iron plssss')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+7', listener_7)

def listener_8():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('we need diams')
    print('we need diams')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+8', listener_8)

def listener_9():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('thx')
    print('thx')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+9', listener_9)

def listener_0():
    keyboard.press_and_release('t')
    time.sleep(0.1)
    keyboard.write('/shout hello')
    print('/shout hello')
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('q')


keyboard.add_hotkey('Ctrl+0', listener_0)

print('开始运行')
keyboard.wait('ctrl+c')

