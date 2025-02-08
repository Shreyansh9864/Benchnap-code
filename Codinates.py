import time

import pyautogui
time.sleep(2)
def display_mouse_coordinates():
    try:

            x, y = pyautogui.position()
            print(f"Mouse coordinates: X = {x}, Y = {y}")
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    display_mouse_coordinates()
