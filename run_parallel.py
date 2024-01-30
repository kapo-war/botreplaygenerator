import subprocess
from concurrent.futures import ThreadPoolExecutor

python_path = '/home/vlab/botvsbot.py'

difficulty = [7, 6, 5, 4, 3]
maps = ["Simple64", "Automaton", "CyberForest", "KairosJunction", 
        "KingsCove", "NewRepugnancy", "PortAleksander", "YearZero"]
levels = {7: "VeryHard", 6: "Harder", 5: "Hard", 4: "MediumHard", 3: "Medium"}


def run_simulation(args):
    subprocess.run(['python', python_path] + args)

def run_all_maps_and_levels():
    script_args = []
    for sc2map in maps:
        for diff in levels.keys():
            for i in range(1):
                script_args.append([sc2map, str(diff)])
    # generate 30 replays each of maps and difficulty   
    for i in range(30):
        with ThreadPoolExecutor() as executor:
            executor.map(run_simulation, script_args)
        print(f"-----------{i} iterate-----------")

def run_by_levels():
    NUM_PARALLEL = 20 
    NUM_ITERATE = 25
    for sc2map in maps:
        for diff in levels.keys():
            script_args = [[sc2map, str(diff)] for _ in range(NUM_PRALLEL)]
            print(script_args)
            for i in range(NUM_ITERATE):
                with ThreadPoolExecutor() as executor:
                    executor.map(run_simulation, script_args)
            result_message = f"{sc2map}:{levels[diff]}"
            line = '-' * (len(result_message) + 22)
            print(f"\n{line}\nFINISH {result_message}\n{line}")
                    
if __name__ == "__main__":
    run_by_levels()
