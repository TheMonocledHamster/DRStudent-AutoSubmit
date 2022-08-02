from DeepRacerStudent import DeepRacerStudent
import json
import time

if __name__ == "__main__":
    with open("./secrets/secrets.json") as config_file:
        config = json.load(config_file)
    control = DeepRacerStudent(config)
    while True:    
        control.submit()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(1500)