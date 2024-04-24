from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import keyboard
import time

virtualKeyboard = KeyboardController()
virtualMouse = MouseController()

spinningButton = 's' 
startButton = 'h'


firstWait = 2 # in seconds
secondWait = .4 # in seconds


print("Listening...")

while True:
    try: 
        
        if keyboard.is_pressed(startButton):
            print('Waiting 2 seconds...')
            time.sleep(firstWait)
            
            print('Spinning...')
            virtualKeyboard.press(spinningButton)
            
            time.sleep(secondWait)
            virtualKeyboard.release(spinningButton)
            
            break
    except:
        break        