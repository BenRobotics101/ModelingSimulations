import requests
import time
import datetime


dt = datetime.datetime.now()

results = open(f"Results_{dt.month}_{dt.day}_{dt.hour}_{dt.minute}_{dt.second}.csv", "w")

for trial in range(30):
    totalBytesDownloaded = 0
    startDownloadTime = time.time()
    r = requests.get('https://codingcando.com/10mb.txt')
    endDownloadTime = time.time()
    if(len(r.text) != 10000000):
        print("Error!")
        print(len(r.text))
        continue
    totalBytesDownloaded = len(r.text)

    timeSpan = endDownloadTime - startDownloadTime

    throughput = totalBytesDownloaded / timeSpan 

    print(f"Trial {trial} download speed: ", throughput)
    results.write(f"{trial},{throughput},{endDownloadTime},{startDownloadTime}\n")

    if(timeSpan < 10):
        time.sleep(10 - timeSpan)

results.close()
