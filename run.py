import subprocess

python_path = '/home/vlab/botvsbot.py'

difficulty = [7, 6, 5, 4, 3]
maps = ["Simple64", "Automation", "CyberForest", "KairosJunction", 
        "KingsCove", "NewRepugnancy", "PortAleksander", "YearZero"]
levels = {7:"VeryHard", 6:"Harder", 5:"Hard", 4:"MediumHard", 3:"Medium"}

for sc2map in maps:
    for diff in levels.keys():
        for i in range(500):
            subprocess.run(['python', python_path] + [sc2map, str(diff)])
