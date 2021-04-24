import logging
import random

from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board
from loderunnerclient.game_client import GameClient

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)


def turn(gcb: Board):
    ladder = gcb.get_ladder_positions() # вызов метода координат лестниц
    # send random one of possible commands

    if has_wall_at():
      act_wall = LoderunnerAction.DRILL_LEFT or LoderunnerAction.DRILL_RIGHT
      return a_wall

    if ladder:
      act_lad =  LoderunnerAction.GO_DOWN or LoderunnerAction.GO_UP
      return act_lad


    while has_enemy_at():
        act_eny =  LoderunnerAction.GO_DOWN or LoderunnerAction.GO_UP or LoderunnerAction.GO_LEFT or LoderunnerAction.GO_RIGHT  or LoderunnerAction.DRILL_LEFT or LoderunnerAction.DRILL_RIGHT
        return act_eny
        
    while has_gold_at:
      act_gold_collect =  LoderunnerAction.GO_LEFT
      return act_gold_collect


def main():
    gcb = GameClient(
        # change this url to your
        "https://dojorena.io/codenjoy-contest/board/player/dojorena471?code=550388707836510351"
    )
    gcb.run(turn)


if __name__ == "__main__":
    main()
