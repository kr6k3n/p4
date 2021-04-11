from .neural_net import Neural_Network
from .simulator import Simulator
from typing import List, Callable, Type, Optional

import time

class Agent:
  """
    Classe de base pour un agent 
  """
  name = "None"
  NN: Optional[Neural_Network]
  def __init__(self,
               SHAPE:   List[int],
               activation_function : Callable,
               sim :  Type[Simulator],
               init_NN: bool=True,
               id:      int = None):
    if init_NN:
      self.NN = Neural_Network(SHAPE, activation_function)
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
  
  def get_action(self, input_vec) -> int:
    nn_output = self.NN.eval_forward(input_vec)
    return nn_output.index(max(nn_output))

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
    game_ended = False
    (print() for _ in range(8))
    while not game_ended:
      game_ended = self.act()
      if debug_game:
        (print("\033[A\033[A") for _ in range(8))
        print(self.sim_instance)
        time.sleep(1)
      if not game_ended:
        game_ended = other.act()
        if debug_game: 
          (print("\033[A\033[A") for _ in range(8))
          print(self.sim_instance)
          time.sleep(1)
    if debug_game: 
      (print("\033[A\033[A") for _ in range(8))
      print(self.sim_instance)
    #assign score ==> should be separate
    self.score += 1 if self.sim_instance.winner == "X" else (-1 if self.sim_instance.winner == "O" else 0.5)
    other.score += 1 if self.sim_instance.winner == "O" else (-1 if self.sim_instance.winner == "X" else 0.5)

  def mutate(self, rate : float) -> None:
    self.NN.mutate(rate)
