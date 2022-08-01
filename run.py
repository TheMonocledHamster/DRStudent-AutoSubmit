import subprocess
import os

# target_dir = os.path.dirname(os.path.abspath(__file__))
target_file = ".\Source\main.py"
subprocess.run("python "+target_file, shell=True)