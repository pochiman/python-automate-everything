import pyautogui

position = pyautogui.position()
print(position)

# pyautogui.moveTo(139, 280, duration=1)
# pyautogui.move(100, 0, duration=1)

# pyautogui.click(clicks=2)
# pyautogui.doubleClick()

# RIGHT-CLICK ON WINDOWS
# pyautogui.click(139, 280, clicks=2)
# pyautogui.click(139, 280, button='right')

# RIGHT-CLICK ON MAC
# pyautogui.click(139, 280)
# pyautogui.dragTo(139, 280, button='right')

pyautogui.moveTo(1326, 567, duration=1)
pyautogui.click()
pyautogui.drag(150, 0, duration=1, button='left')
pyautogui.drag(0, -150, duration=1, button='left')
pyautogui.drag(-150, 0, duration=1, button='left')
pyautogui.drag(0, 150, duration=1, button='left')
