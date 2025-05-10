""" webbrowser - Open web pages using the default browser directly """

# 1. Open URL from Default Browser
import webbrowser
webbrowser.open("https://www.python.org")

# 2. Open a URL with a Specific Browser - must USE %s at the END of the path
import webbrowser
path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Browsers .exe
# %s divided Path and URL for the script 
webbrowser.get(path).open("https://www.github.com") 

# 3. Opens the URL in a New Window - (open seperate main window for this)
import webbrowser
webbrowser.open_new("https://www.python.org")
 
# 4. Open a URL in a New Tab - (on the same main window)
import webbrowser
webbrowser.open_new_tab("https://www.github.com")

