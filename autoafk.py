import keyboard
import random
import time
time.sleep(10)
for i in range(100):
    t = random.randint(1,5)
    print(t)
    if t==1:
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
    elif t==2: 
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')
    elif t==3: 
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')
    elif t==4: 
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.release('w')
    else:
        keyboard.press('space')
        time.sleep(0.2)
        keyboard.release('space')
    time.sleep(60)