'''  .subprocess()  - Run and manage, System commands (CMD/PowerShell) or External programs.

# --- Key Notes 
# List format preferred → subprocess.run(["echo", "Hello"])  → replace spaces with comma ( , )
# Use raw strings (r"") for Windows paths

      shell=True      → only for Batch Script File Run or Command Run (for Raw - subprocess.run("echo %PATH%") )
  capture_output=True  → capture the output of the teminal
      text=True      → convert the above capture into Python String format

  stdout (Standard Output): Where a program sends its normal output (e.g., print statements).
  stderr (Standard Error): Where a program sends error messages (e.g., warnings, exceptions).
'''

# Open or Ping URLs
import subprocess
subprocess.run(["start", "https://google.com"], shell=True)  # Open URL
subprocess.run(["ping", "google.com"])  # ping URL


# Open Programs or Files (Softwares)
import subprocess
subprocess.run(["notepad", r"C:\User\Desktop\file.txt"])  # Open specific file
subprocess.run(["explorer", r"C:\Windows"])  # Open File Explorer
subprocess.run(["notepad"])  # open program


# Run Terminals (CMD/PowerShell)
import subprocess
subprocess.run(["cmd", "/c", "dir /w"])  # CMD  → ( /w - just names ) 
subprocess.run(["powershell", "ls"])  # PowerShell


# Direct Run on Terminals and Get their Output

# 1. Simple command with output
# run in CMD shell / capture the output / convert output to python string
import subprocess  
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
# resuls -  captured output assigned to the variable 
print(result.stdout)   # .stderr
print(result)

# 1.2. Same with   "cmd", "/c",   |accept shell=True
import subprocess  
result1 = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result1.stdout)


# 2. 

# 3. Running a .bat file (Windows) or .sh file (Linux/macOS).
import subprocess
subprocess.run("mybatchs.bat", shell=True)
 

