''' .time() - handle the programs which need : time / delays / calculate times '''

# 1. time.sleep(seconds) -> Add delay to program
import time
time.sleep(3)  #(3.5) = 3.5 sec 
print("Wait 3 seconds...")


# 2. time.ctime() -> Current time on the Device (just-Display)
import time
print(time.ctime())  # Sun May 11 23:37:16 2025


# 3. time.perf_counter() -> Stopwatch / (just-high-resolution-timer)
import time
start = time.perf_counter()
time.sleep(1.8853)  # 1.8853 sec -> 1.89 sec
end = time.perf_counter()
print(f"{end - start:.2f} seconds gone")


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

# 6. time.time() -> Time in seconds (float) from Epoch(January 1, 1970) - (timestamps and general date/time purposes)
import time
print(time.time())  # Example output: 1715394410.502188

