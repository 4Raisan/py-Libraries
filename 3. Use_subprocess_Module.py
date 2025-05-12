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

#---. .run > Terminals + Just Open BATs / Run .------------------------------------------------------

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
print(result.stdout)  # clean,structured output  
print(result.stderr)  # Only shows error messages if the command failed (scroll down for errors)
print(result)  # whole process for the output

# 2. Terminal Runs with outputs - with   "cmd", "/c",   |accept shell=True > mention terminal on the code
import subprocess  
result1 = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result1.stdout)  # .stderr
print(result1)


#---. timeout=seconds > Timeouts .----------------------------------------------------------------

# 3. Timeout Control -[  timeout=#  ]
import subprocess
subprocess.run(["dir"], shell=True, timeout=5) # only give command 5 seconds to execute, then kill it -(if it's not ended)


# ---. Error checking -[  Exception as e  ]  .-----------------------------------------------------

# 4. ALL erros 
import subprocess
try:
    subprocess.run(["dir"], shell=True)  # give max execution time of 5 Seconds
except Exception as e:
    print(f"Error is here ({e})")
'''
subprocess.TimeoutExpired   -> Command ran too long
subprocess.CalledProcessError   -> Command failed (non-zero exit code)
FileNotFoundError   -> Command doesn't exist
PermissionError   -> No execute permission
ValueError   -> Invalid arguments passed
'''

# check=True  -:-  Check File existance > CalledProcessError  ->  # print error itself : if None Zero
import subprocess
try:                                                                      
    subprocess.run(["dir", r"C:\User\file.txt"], shell=True, check=True)   
except (subprocess.CalledProcessError) :                 
    print("CalledProcessError")

# timeout=seconds  -:-  Give time to execute > TimeoutExpired  ->  # print error itself : if None Zero
import subprocess
try:
    subprocess.run(["dir"], shell=True, timeout=0.00001)  # give max execution time of 5 Seconds
except (subprocess.TimeoutExpired):
    pass  # null operation - it does nothing when executed.


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
