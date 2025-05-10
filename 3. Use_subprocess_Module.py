'''  .subprocess()  - Run and manage, System commands (CMD/PowerShell) or External programs.  '''

# Ping URLs
import subprocess
subprocess.run(["ping", "google.com"])

# Open Programs (Softwares)
import subprocess
subprocess.run(["notepad"])

# Run Terminals (CMD/PowerShell)
import subprocess
subprocess.run(["cmd", "/c", "dir /w"])  # CMD
subprocess.run(["powershell", "ls"])  # PowerShell
