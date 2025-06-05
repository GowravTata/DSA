import pyautogui
import time

# Interval between movements (in seconds)
interval = 10  # Move mouse every 60 seconds

try:
    print("Starting mouse movement loop. Press Ctrl+C to stop.")
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y, duration=0.1)
        pyautogui.moveTo(x, y, duration=0.1)
        print(f"Moved mouse at {time.strftime('%H:%M:%S')}")
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nMouse movement stopped by user.")
