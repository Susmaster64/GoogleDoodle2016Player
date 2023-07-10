import random
import time
from pynput.mouse import Button, Controller
import keyboard
import pyautogui
mouse = Controller()

def move_mouse_to_destination(x_dest, y_dest):
    start = time.time()
    x_start, y_start = mouse.position
    
    # Calculate 3 random points on the path from start to destination
    points = []
    for i in range(3):
        # Calculate the position of the current point
        x_current = int(x_start + ((x_dest - x_start) / 3) * i)
        y_current = int(y_start + ((y_dest - y_start) / 3) * i)
        
        # Deviate the point slightly
        x_deviation = random.randint(-3, 3)
        y_deviation = random.randint(-3, 3)
        x_current += x_deviation
        y_current += y_deviation
        
        # Add the deviated point to the list
        points.append((x_current, y_current))
        

    # Move the mouse through each point in order
    for point in points:
        pyautogui.moveTo(point[0], point[1],_pause=False)
    
    # Move the mouse to the destination
    pyautogui.moveTo(x_dest, y_dest,_pause=False)
    end = time.time()
    print(f'Function completed in {end - start} seconds')


def red():
    mouse = Controller()
    mouse.press(Button.left)
    destination_x = mouse.position[0]+50
    destination_y = mouse.position[1]+2
    move_mouse_to_destination(destination_x, destination_y)
    mouse.release(Button.left)
    print('Red')


def blue():

    mouse.press(Button.left)
    destination_x = mouse.position[0]+2
    destination_y = mouse.position[1]+50
    move_mouse_to_destination(destination_x, destination_y)
    mouse.release(Button.left)
    print('Blue')


def green():

    mouse.press(Button.left)
    destination_x = mouse.position[0]+20
    destination_y = mouse.position[1]-25
    move_mouse_to_destination(destination_x, destination_y)
    destination_x = mouse.position[0]+20
    destination_y = mouse.position[1]+25
    move_mouse_to_destination(destination_x, destination_y)
    mouse.release(Button.left)
    print('Green')


def yellow():

    mouse.press(Button.left)
    destination_x = mouse.position[0]-20
    destination_y = mouse.position[1]+25
    move_mouse_to_destination(destination_x, destination_y)
    destination_x = mouse.position[0]-20
    destination_y = mouse.position[1]-25
    move_mouse_to_destination(destination_x, destination_y)
    mouse.release(Button.left)
    print('yellow')


def lightning():

    mouse.press(Button.left)
    destination_x = mouse.position[0]+30
    destination_y = mouse.position[1]+20
    move_mouse_to_destination(destination_x, destination_y)
    destination_x = mouse.position[0]-30
    destination_y = mouse.position[1]+20
    move_mouse_to_destination(destination_x, destination_y)
    destination_x = mouse.position[0]+30
    destination_y = mouse.position[1]+20
    move_mouse_to_destination(destination_x, destination_y)
    mouse.release(Button.left)
    print('Lightning')

time.sleep(3)

while keyboard.is_pressed('q') == False:
    red()
    mouse.position = (960, 540)
    time.sleep(0.005)
    blue()
    mouse.position = (960, 540)
    time.sleep(0.005)
    green()
    mouse.position = (960, 540)
    time.sleep(0.005)
    yellow()
    mouse.position = (960, 540)
    time.sleep(0.005)
    lightning()
    mouse.position = (960, 540)
    time.sleep(0.005)
'''
while 1:
    
    if keyboard.is_pressed('q') == True:
        red()
        mouse.position = (960, 540)
        while keyboard.is_pressed('q') == True:
            time.sleep(0.01)
        
    elif keyboard.is_pressed('w') == True:
        blue()
        mouse.position = (960, 540)
        while keyboard.is_pressed('w') == True:
            time.sleep(0.01)
    elif keyboard.is_pressed('e') == True:
        green()
        mouse.position = (960, 540)
        while keyboard.is_pressed('e') == True:
            time.sleep(0.01)
    elif keyboard.is_pressed('r') == True:
        yellow()
        mouse.position = (960, 540)
        while keyboard.is_pressed('r') == True:
            time.sleep(0.01)
    elif keyboard.is_pressed('t') == True:
        lightning()
        mouse.position = (960, 540)
        while keyboard.is_pressed('t') == True:
            time.sleep(0.01)
'''
