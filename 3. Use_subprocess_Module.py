'''  .subprocess()  - Run and manage, System commands (CMD/PowerShell) or External programs.  '''
# --- Key Notes 
# List format preferred → subprocess.run(["echo", "Hello"])  → replace spaces with comma ( , )
# Use raw strings (r"") for Windows paths
#  shell=True  → only for Batch Script File Run or Command Run (for Raw - subprocess.run("echo %PATH%") )
#  capture_output=True  → capture the output of the teminal
#  text=True  → convert the above capture into Python String format

# Ping URLs
import subprocess
subprocess.run(["ping", "google.com"])

# Open Programs (Softwares)
import subprocess
subprocess.run(["notepad"])

# Run Terminals (CMD/PowerShell)
import subprocess
subprocess.run(["cmd", "/c", "dir /w"])  # CMD  → ( /w - just names ) 
subprocess.run(["powershell", "ls"])  # PowerShell


# Direct Run on Terminals and Get their Output

# 1. Simple command with output
# run in CMD shell / capture the output / convert output to python string
import subprocess  
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(result.stdout)

# 3. Running a .bat file (Windows) or .sh file (Linux/macOS).
import subprocess
subprocess.run("mybatchs.bat", shell=True)
 

