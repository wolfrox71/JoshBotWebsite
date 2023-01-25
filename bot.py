from status import status
import time

file = status("status.txt")

while (file.get_status() in status.RUNNING_STATUSES):
    print("Running")
    time.sleep(1)