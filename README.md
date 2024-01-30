# Get StarCraft II & maps
Download Starcraft2 linux package 4.8.6 in https://github.com/Blizzard/s2client-proto

We aim to get bot vs bot replay data in Simple64 and maps from 2019 season1.
Download Melee and Ladder 2019 Season 1 map packs and extract them to your `StarCraftII/Maps/` directory.

# PySC2
```
$git clone https://github.com/deepmind/pysc2.git
$pip install --upgrade pysc2/
```
You should delete `extra_ports=self._ports` part located in line 338 of `pysc2\pysc2\env\sc2_env.py`

![image](https://github.com/kapo-war/botreplaygenerator/assets/67684178/8a3ba5f8-c92b-465d-87e3-05aec87c19fe)

or just download using pip install pysc2=4.0.0

# Generate Bot vs Bot Replays
Prepare botvsbot.py and run_parallel.py
Generate directory like this or change save_path in botvsbot.py
```
/sc2-dataset/BotvsBotReplay/Automaton
/sc2-dataset/BotvsBotReplay/CyberForest
/sc2-dataset/BotvsBotReplay/KairosJunction
/sc2-dataset/BotvsBotReplay/KingsCove
/sc2-dataset/BotvsBotReplay/NewRepugnancy
/sc2-dataset/BotvsBotReplay/PortAleksander
/sc2-dataset/BotvsBotReplay/Simple64
/sc2-dataset/BotvsBotReplay/YearZero
```
Change the parallel option in run_parallel.py and run.

