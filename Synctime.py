import subprocess  
import time  
import sys

#Function to disable time synchronization.
def disable_time_sync():
    print("Disabling time synchronization...")
    subprocess.run(["w32tm", "/config", "/manualpeerlist:\"\"", "/syncfromflags:NO_SYNC", "/reliable:NO", "/update"], check=True)# Execute the command to disable time synchronization
    subprocess.run(["net", "stop", "w32time"], check=True)# Stop the Windows Time service
    print("Time synchronization disabled.")

#Function to enable time synchronization.
def enable_time_sync():
    print("Enabling time synchronization...")
    subprocess.run(["w32tm", "/resync"], check=True)# Execute the command to force time synchronization
    subprocess.run(["net", "start", "w32time"], check=True)# Start the Windows Time service
    print("Time synchronization enabled.")

if __name__ == "__main__":
    disable_time_sync()
    time.sleep(2)  
    enable_time_sync()
    sys.exit()