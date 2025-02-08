import pyautogui
import math
import time
time.sleep(10)
# Set the center and radius of the circle
center_x, center_y =  984, 545
radius = 100

# Calculate points along the circle's circumference
num_points = 100
angle_step = 2 * math.pi / num_points
circle_points = [(center_x + int(radius * math.cos(angle)), center_y + int(radius * math.sin(angle))) for angle in
                 [i * angle_step for i in range(num_points)]]

# Move the mouse cursor to each point to simulate drawing the circlezzz
pyautogui.dragTo(circle_points[0][0], circle_points[0][1], duration=0.25)
for point in circle_points[1:]:
    pyautogui.dragTo(point[0], point[1], duration=0.05)

# Add a delay before moving the mouse away
time.sleep(2)

# Move the mouse cursor away
pyautogui.moveTo(0, 0)
