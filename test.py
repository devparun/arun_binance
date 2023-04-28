import time, datetime
while True:
    print(f'Time Now : {datetime.datetime.now()}', end='\r', flush=True)
    time.sleep(1)
