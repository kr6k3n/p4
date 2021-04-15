from .neural_net import Neural_Network, Network_Description
from .simulator import Simulator


from typing import Type, Optional
import numpy as np

import time


def clear_board():
  for _ in range(8):
    print("\033[A\033[A")

class Agent:
  """
    Classe de base pour un agent 
  """
  name = "None"
  NN: Optional[Neural_Network]
  def __init__(self,
               description : Network_Description,
               sim         : Type[Simulator],
               init_NN     : bool=True,
               id          : int = None):

    if init_NN:
      self.NN = Neural_Network(description=description)
    else:
      self.NN = None
    if not id is None:
      self.id = id
    self.sim = sim
    self.sim_instance : Optional[Simulator] = None
    self.score : float = 0
    self.player_id : Optional[str] = None

  def reset(self):
    self.score = 0

  def get_action(self, input_vec : np.ndarray) -> int:
    nn_output = self.NN.eval_forward(input_vec)
    # print(int(np.argmax(nn_output)), np.argmax(nn_output))    
    return int(np.argmax(nn_output))

  def act(self) -> bool:
    current_state = self.sim_instance.serialized_state(self.player_id)
    action = self.get_action(current_state)
    return self.sim_instance.act(action)

  def play_against_other(self, other, debug_game=False) -> None:
    self.player_id = "X"
    other.player_id = "O"
    #create shared simulator
    new_sim = self.sim()
    other.sim_instance = new_sim
    self.sim_instance  = new_sim
    # play all game turns
    if debug_game:
      print("\n"*8)
    game_ended = False
    while not game_ended:
      game_ended = self.act()
      if debug_game:
        clear_board()
        print(self.sim_instance)
        if not game_ended: time.sleep(0.5)
      if not game_ended:
        game_ended = other.act()
        if debug_game: 
          clear_board()
          print(self.sim_instance)
          if not game_ended: time.sleep(0.5)
    #assign score ==> should be separate
    self.score += 1 if self.sim_instance.winner == "X" else (-1 if self.sim_instance.winner == "O" else 0.5)
    other.score += 1 if self.sim_instance.winner == "O" else (-1 if self.sim_instance.winner == "X" else 0.5)

  def mutate(self, rate : float) -> None:
    self.NN.mutate(rate)
