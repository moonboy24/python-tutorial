import time
from datetime import datetime

def task():
    # This the code that runs every 2 minutes
    with open("time_log.txt" , "a") as f:
        f.write(f"Script ran at : {datetime.now()}\n")
    print(f"Task ran at : {datetime.now()}")
    
while True:
    task()
    time.sleep(30)