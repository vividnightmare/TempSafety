#
##########
#
#   Simple program to protect against ovherheat
#
#   Set username to whatever user has the crypto pedal through the floor
#
#   Run as a different user with privilege to kill
#
#########
#


import os
import time
import psutil


print("----------")


while True:
    
    username = ""
    
    temp = psutil.sensors_temperatures()
    cputemp = []
    for name, entries in temp.items():
        for entry in entries:
            cputemp.append(entry.current)
    hightemp = max(cputemp)
    print("".join(["Temp: ", str(hightemp), "C"])

    if hightemp >= 85:
        for proc in psutil.process_iter():
            if proc.username() == username:
                print("".join(["Killing process ", str(proc.pid)])
                os.kill(proc.pid, 9)
    
    print("----------")
    time.sleep(5)
    
