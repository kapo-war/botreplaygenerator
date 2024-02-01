# Get StarCraft II & maps
- Download Starcraft2 linux package 4.8.6 in https://github.com/Blizzard/s2client-proto

- We aim to get bot vs bot replay data in Simple64 and maps from 2019 season1.
- Download Melee and Ladder 2019 Season 1 map packs and extract them to your `StarCraftII/Maps/` directory.

# PySC2
```
$git clone https://github.com/deepmind/pysc2.git
$pip install --upgrade pysc2/
```
You should delete `extra_ports=self._ports` part located in line 338 of `pysc2\pysc2\env\sc2_env.py`

or just download using `$pip install pysc2=4.0.0`

# Generate Bot vs Bot Replays
- Prepare `botvsbot.py` and `run_parallel.py`
- Change `ROOT_PATH` in `botvsbot.py` and `PYTHON_PATH` in `run_parallel.py`
- Change the parallel option `NUM_PARALLEL, NUM_ITERATE` in `run_parallel.py` and run.

# Transform the Bot vs Bot replays
- Change previous `transform_replay_data.py` into new above one
- Prepare `autotransform.py` and change `PATH1`, `PATH2`, then run
