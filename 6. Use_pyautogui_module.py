''' pyautogui -> used to automate keyboard, mouse actions and etc. 
pip install pyautogui '''

# Type text (Mouse cursor should be active on the Typable place)
pyautogui.write("Hello, world!", interval=0.1)   # interval, for each character 

# Move the mouse to coordinates (100, 100)
pyautogui.moveTo(100, 100, duration=1)

# Click the mouse -> default click on the mouse location 
# -> specified location:  pyautogui.click(x=100, y=350)
pyautogui.click()  # single click
pyautogui.rightClick()  # right click
pyautogui.middleClick()  # middle click

# Screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png") # default > "C:\Users\4Raisan\screenshot.png"
