import os
import time
import subprocess

# Define the name of the process to check
process_name = "Grammarly.Desktop.exe"

# Define the time to wait before the script ends
wait_time = 60  # seconds

# Start the timer
start_time = time.time()

while True:
    # Get the list of all processes
    process_list = subprocess.check_output(['tasklist']).decode().split('\n')

    # Check if the process is running
    if any(process_name in process for process in process_list):
        print("Loading Grammarly+")

    # Check if the wait time has passed
    if time.time() - start_time > wait_time:
        break

    # Wait for a short period of time before checking again
    time.sleep(1)
