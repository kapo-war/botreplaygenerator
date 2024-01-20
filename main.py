from absl import app
from pysc2 import maps
from pysc2 import run_configs
from pysc2.tests import utils
from s2clientprotocol import common_pb2 as sc_common
from s2clientprotocol import sc2api_pb2 as sc_pb


def main(unused_argv):
    run_config = run_configs.get(version="4.8.6")
    #edit this part to change map
    map_inst = maps.get("Simple64")

    with run_config.start(want_rgb=False) as controller:
        create = sc_pb.RequestCreateGame(local_map=sc_pb.LocalMap(map_path=map_inst.path, map_data=map_inst.data(run_config)))

        # edit this part to change bot setting
        # dfficulty: VeryEasy < Easy < Medium < MediumHard < Hard < Harder < VeryHard
        create.player_setup.add(
            type=sc_pb.Computer, race=sc_common.Random, difficulty=sc_pb.VeryHard)
        create.player_setup.add(
            type=sc_pb.Computer, race=sc_common.Random, difficulty=sc_pb.Hard)

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
        run_config.save_replay(controller.save_replay(), "/home/vlab/pysc2/bot_bot_replay")


if __name__ == "__main__":
  app.run(main)
