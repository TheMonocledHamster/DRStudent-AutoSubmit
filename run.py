import subprocess
import time

while True:
    try:
        target_file = ".\Source\main.py"
        subprocess.run("python "+target_file, shell=True)
        time.sleep(1500)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except:
        time.sleep(30)
        continue