import os
import time
from datetime import datetime


repo_path = r"C:\Users\Administrator\Documents\autocommit\test"
commit_message = "Commit automático em " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
intervalo = 60 * 1 

while True:
    os.chdir(repo_path)
    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push origin main")

    print(f"Commit realizado: {commit_message}")
    time.sleep(intervalo)
