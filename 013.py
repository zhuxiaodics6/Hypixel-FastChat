import time
import keyboard
from pynput.mouse import Controller, Button
mouse = Controller()
# 模拟左键点击



def start_keyboard_listener():
    """
    开始键盘监听的回调函数
    """
    print("start")
    time.sleep(1)
    print("start")
    st = time.time()
    n = 30
    for i in range(n):
        mouse.click(Button.left)
        keyboard.release('shift')
        keyboard.press('s') if i!=(n-1) else None
        time.sleep(0.2175) if i!=(n-1) else None
        keyboard.press('shift') if i!=(n-1) else None
        time.sleep(0.11) if i!=(n-1) else None
        keyboard.release('s') if i!=(n-1) else None
        print(i)
        mouse.click(Button.left)
    mouse.click(Button.left)
    keyboard.release('s, shift')
    print(time.time()-st)
    print('stop')



keyboard.add_hotkey('Ctrl+Shift+Alt', start_keyboard_listener)

try:
    keyboard.wait('ctrl+c')
except KeyboardInterrupt:
    ...