from absl import app
from pysc2 import maps
from pysc2 import run_configs
from pysc2.tests import utils
from s2clientprotocol import common_pb2 as sc_common
from s2clientprotocol import sc2api_pb2 as sc_pb
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("map", type=str, help='"Simple64", "Automaton", "CyberForest", "KairosJunction", "KingsCove", "NewRepugnancy", "PortAleksander", "YearZero"')
parser.add_argument("difficulty", type=int, help="VeryHard:7, Harder:6, Hard:5, MediumHard:4, Medium:3")
args = parser.parse_args()

ROOT_PATH = "/sc2-dataset/BotvsBotReplay/" # edit this root path

levels = {7:"VeryHard", 6:"Harder", 5:"Hard", 4:"MediumHard", 3:"Medium"}

def main(unused_argv):
    run_config = run_configs.get(version="4.8.6")
    map_inst = maps.get(args.map)

    with run_config.start(want_rgb=False) as controller:
        create = sc_pb.RequestCreateGame(local_map=sc_pb.LocalMap(map_path=map_inst.path, map_data=map_inst.data(run_config)))
        """
        class BotBuild(enum.IntEnum):
            random = sc_pb.RandomBuild
            rush = sc_pb.Rush
            timing = sc_pb.Timing
            power = sc_pb.Power
            macro = sc_pb.Macro
            air = sc_pb.Air
        """
        create.player_setup.add(
            type=sc_pb.Computer, race=sc_common.Protoss, difficulty=args.difficulty, ai_build=sc_pb.RandomBuild)
        create.player_setup.add(
            type=sc_pb.Computer, race=sc_common.Protoss, difficulty=args.difficulty, ai_build=sc_pb.RandomBuild)
        create.player_setup.add(type=sc_pb.Observer)
        controller.create_game(create)
        join = sc_pb.RequestJoinGame(
            options=sc_pb.InterfaceOptions(),
            observed_player_id=0)
        controller.join_game(join)

        # time limit 3600s => edit this to change time limit
        for _ in range(3600):
            controller.step(16)
            obs = controller.observe()
            if obs.player_result:
                for r in obs.player_result:
                    print(f"Player {r.player_id}: {sc_pb.Result.Name(r.result)}")
                break

        # save replay => edit save directory
        save_path = os.path.join(ROOT_PATH, args.map, levels[args.difficulty])
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        run_config.save_replay(controller.save_replay(), save_path)

if __name__ == "__main__":
  app.run(main)
