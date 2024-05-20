from ahk import AHK
import pyautogui
ahk = AHK()


# ahk.mouse_drag(100, 100, relative=True) # Holds down primary button and moves the mouse

#
# print(pyautogui.size())
pyautogui.mouseDown()
# pyautogui.moveTo(900, 150)


pyautogui.moveTo(900, 900, duration=2)  # move mouse to XY coordinates over num_second seconds
# pyautogui.moveRel(900, 0, duration=2)  # move mouse relative to its current position