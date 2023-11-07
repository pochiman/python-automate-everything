import pyautogui
import time

position = pyautogui.position()
print(position)

pyautogui.doubleClick(132, 200)
time.sleep(1)
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('Python is good too!\n')

pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
pyautogui.press(5*['down'])
pyautogui.hotkey('command', 'v')
