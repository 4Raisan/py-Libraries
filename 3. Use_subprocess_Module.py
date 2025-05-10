'''  .subprocess()  - Run and manage, System commands (CMD/PowerShell) or External programs.  '''
# --- Key Notes 
# List format preferred → subprocess.run(["echo", "Hello"])  → replace spaces with comma ( , )
# Use raw strings (r"") for Windows paths
#  shell=True  → only for Batch Script File Run or Command Run (for Raw - subprocess.run("echo %PATH%") )

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



