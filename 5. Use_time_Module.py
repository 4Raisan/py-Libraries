''' .time() - handle the programs which need : time / delays / calculate times '''

# Epoch  =>  January 1, 1970

# 1. time.time() -> Time in seconds (float) from Epoch -- can be use to calculation EASY with float seconds
import time
print(time.time())  # Example output: 1715394410.502188

# 2. time.sleep(seconds) -> Add delay to program
import time
time.sleep(3)
print("Wait 3 seconds...")

# 3. time.ctime() -> Current time on the Device
import time
print(time.ctime())           # Current time
