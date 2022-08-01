from DeepRacerStudent import DeepRacerStudent
import json

if __name__ == "__main__":
    with open("./secrets/secrets.json") as config_file:
        config = json.load(config_file)
    control = DeepRacerStudent(config)
    control.submit()