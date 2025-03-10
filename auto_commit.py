import random
from datetime import datetime, timedelta
import os

# Define o dia atual
today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# Escolhe a janela de tempo
if random.random() < 0.3:
    start_hour = 13
    end_hour = 19
else:
    start_hour = 8
    end_hour = 16

start_time = today.replace(hour=start_hour, minute=0)
end_time = today.replace(hour=end_hour, minute=0)

# Número de commits
num_commits = random.randint(20, 80)

# Gera horários
commit_times = []
for _ in range(num_commits):
    random_seconds = random.randint(0, int((end_time - start_time).total_seconds()))
    commit_time = start_time + timedelta(seconds=random_seconds)
    commit_times.append(commit_time)
commit_times.sort()

# Faz os commits
for i, commit_time in enumerate(commit_times):
    with open("auto_commit_log.txt", "a") as f:
        f.write(f"Commit {i+1} às {commit_time.strftime('%H:%M:%S')}\n")
    os.system(f'git add auto_commit_log.txt')
    os.system(f'git commit -m "Auto commit {i+1} às {commit_time.strftime('%H:%M:%S')}"')