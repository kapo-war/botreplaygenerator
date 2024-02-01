import os
import torch
import numpy as np
import random

seed = 0  # use the fixed seed for the full program

# must use
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed(seed)
torch.cuda.manual_seed_all(seed)  # if you are using multi-GPU.

os.environ['PYTHONHASHSEED'] = str(seed)

import alphastarmini
from alphastarmini.core.sl import load_pickle
import param as P
from alphastarmini.core.sl import transform_replay_data

PATH1 = "/sc2-dataset/BotvsBotReplay/" # root path of replay data
PATH2 = "/home/vlab/BotvsBotTensor/" # root path for saving data
levels = {7:"VeryHard", 6:"Harder", 5:"Hard", 4:"MediumHard", 3:"Medium"}
maps = ["Simple64", "Automaton", "CyberForest", "KairosJunction", 
        "KingsCove", "NewRepugnancy", "PortAleksander", "YearZero"]

if __name__ == '__main__':
    for sc2map in maps:
        for level in levels.keys():
            replay_path = os.path.join(PATH1, sc2map, levels[level])
            files = os.listdir(replay_path)
            data_num = len(files)
            save_path = os.path.join(PATH2, sc2map, levels[level])
            if not os.path.exists(save_path):
                os.makedirs(save_path) 
            transform_replay_data.test(data_num=data_num, replay_path=replay_path, save_path=save_path + '/')

            result_message = f"{sc2map}:{levels[level]}"
            line = '-' * (len(result_message) + 22)
            print(f"\n{line}\nFINISH {result_message}\n{line}")
