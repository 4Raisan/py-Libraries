'''  .subprocess()  - Run and manage, System commands (CMD/PowerShell) or External programs.

# --- Key Notes 
# List format preferred → subprocess.run(["echo", "Hello"])  → replace spaces with comma ( , )
# Use raw strings (r"") for Windows paths

      shell=True      → only for Batch Script File Run or Command Run (for Raw - subprocess.run("echo %PATH%") )
  capture_output=True  → capture the output of the teminal ( no echo 's are captured, only dir like once )
      text=True      → convert the above capture into Python String format

  stdout (Standard Output): Where a program sends its normal output (e.g., print statements).
  stderr (Standard Error): Where a program sends error messages (e.g., warnings, exceptions).
'''

#---. Terminals + Just Open BATs / Run .------------------------------------------------------

# Running a .bat file (Windows) or .sh file (Linux/macOS).
import subprocess
subprocess.run("mybatchs.bat", shell=True)

# Directly Run on Terminals (CMD/PowerShell) - No Outputs
import subprocess
subprocess.run(["cmd", "/c", "dir /w"])  # CMD  → ( /w - just names ) 
subprocess.run(["powershell", "ls"])  # PowerShell

#---. Terminals with Outputs .------------------------------------------------------------------

# 1. Terminal Runs with outputs
# run in CMD shell / capture the output / convert output to python string
import subprocess  
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
# resuls -  captured output assigned to the variable 
print(result.stdout)   # .stderr
print(result)

# 2. Terminal Runs with outputs - with   "cmd", "/c",   |accept shell=True
import subprocess  
result1 = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result1.stdout)  # .stderr
print(result1)

#---. try:except: - Timeouts + Errors .----------------------------------------------------------------

# 3. Timeout Control -[  timeout=#  ]
try:
      subprocess.run(["dir"], shell=True, timeout=5)  # give time to commands
except (subprocess.TimeoutExpired):
      print("TimeOut")
      
# 4. Error checking -[  check=True  ]
try:
      subprocess.run(["dir", "fileX"], shell=True, check=True)  # check FileX's existing 
except (subprocess.CalledProcessError):
      print("Command failed")

#---. File/Program Handling + URLs .-------------------------------------------------------------------

# Open Programs or Files (Softwares)
import subprocess
subprocess.run(["notepad", r"C:\User\Desktop\file.txt"])  # Open specific file
subprocess.run(["explorer", r"C:\Windows"])  # Open File Explorer
subprocess.run(["notepad"])  # open program

# Open or Ping URLs
import subprocess
subprocess.run(["start", "https://google.com"], shell=True)  # Open URL
subprocess.run(["ping", "google.com"])  # ping URL
