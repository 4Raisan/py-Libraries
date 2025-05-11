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

''' .time() - handle the programs which need : time / delays / calculate times '''

# Epoch  =>  January 1, 1970

# 1. time.time() -> Time in seconds (float) from Epoch -- can be use to calculation EASY with float seconds
import time
print(time.time())  # Example output: 1715394410.502188


# 2. time.sleep(seconds) -> Add delay to program
import time
time.sleep(3)
print("Wait 3 seconds...")


# 3. time.ctime() -> Current time on the Device (just-Display)
import time
print(time.ctime())  # Sun May 11 23:37:16 2025


# 4. time.localtime(),tm_...  -> Current time on the Device (Calculations with variables)
import time
print(time.localtime())
# Output: time.struct_time(tm_year=2025, tm_mon=5, tm_mday=11, tm_hour=23, tm_min=48, tm_sec=5, tm_wday=6, tm_yday=131, tm_isdst=0)
print(time.localtime().tm_mon , time.localtime().tm_mon)
# Output: 5 11
'''  
tm_year -> Year  /  tm_mon  -> Month   /  tm_mday -> Day
tm_hour -> Hour  /  tm_min  -> Minute  /  tm_sec  -> Second
tm_wday -> Week of the day ( 0 for Monday)
tm_yday -> Day of the Year
tm_isdst=0  -> Daylight Saving Time  # (mostly 0-No) or 1 (add 1-Hour)
'''


# 5. time.strftime("%format") -> format device time (Display)
import time
print(time.strftime("%Y-%m-%d, %I %p"))
# Output: 2025-05-12, 12 AM
'''
 %Y	 ->  Year
 %m	 ->  Month
 %d	 ->  Day (Number)
 %H	 ->  Hour (24H)
 %I	 ->  Hour (12H)
 %M	 ->  Minute 
 %S	 ->  Second
 %A	 ->  Weekday (Sunday)
 %p	 ->  AM / PM	
'''



