''' pyautogui -> used to automate keyboard, mouse actions and etc. 
pip install pyautogui '''

# ⚠️ Safety Tip: If your script gets stuck in a loop or misbehaves, move your mouse cursor to the top-left corner of the screen,
#                 to trigger an emergency fail-safe.

#----- Keyboard Control --------------------------------------------------------------

# Type text (Mouse cursor should be active on the Typable place)
pyautogui.write("Hello, world!", interval=0.1)   # interval, for each character 

""" KEYS with .press() :::
'a' - 'z'  /  '0' - '9'  /  'f1' - 'f9'
'enter' / 'space' / 'backspace'
'tab' / 'esc' / 'delete'
'alt' / 'altleft' / 'altright'
'ctrl' / 'ctrlleft' / 'ctrlright'
'shift' / 'shiftleft' / 'shiftright'
'capslock' / 'numlock' / 'scrolllock'
'up' / 'down' / 'right' / 'left' 
'win' / 'winleft' / 'winright' / 'command'
'home' / 'insert' / 'end'
'pageup' / 'pagedown' / 'pause' / 'printscreen' """

# Press a key > pyautogui.press('')
pyautogui.press('enter')



#----- Mouse Control --------------------------------------------------------------

# Move the mouse to coordinates (100, 100)
pyautogui.moveTo(100, 100, duration=1)  # just appear on the location
pyautogui.dragTo(400, 500)  # act like physical mouse going

# Click the mouse -> default click on the mouse location 
# -> specified location:  pyautogui.click(x=100, y=350)
pyautogui.click()  # single click
pyautogui.rightClick(x=400, y=600)  # right click
pyautogui.middleClick()  # middle click

# Scroll(amount)  amount > 0 for up/right  |  amount < 0 for down/left
# vertically |
pyautogui.scroll(200)    # Scroll up
pyautogui.scroll(-200)   # Scroll down
# horizontally --
pyautogui.hscroll(200)    # Scroll right
pyautogui.hscroll(-200)   # Scroll left

#-------------------------------------------------------------------------------------

# Screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png") # default >  r"C:\Users\4Raisan\screenshot.png"
