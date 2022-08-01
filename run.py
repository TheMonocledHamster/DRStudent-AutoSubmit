import subprocess
import time

while True:
    target_file = ".\Source\main.py"
    subprocess.run("python "+target_file, shell=True)
    time.sleep(1800)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))