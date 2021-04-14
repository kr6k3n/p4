from src.learning.activation_functions import ReLu, Sigmoid
from .learning.agent import Agent

from .p4_simulator import P4Simulator

input_size = 7*6

DESCRIPTION = [
              (input_size,    None),
              (input_size//2, ReLu),
              (input_size//2, ReLu),
              (input_size//2, ReLu),
              (input_size//2, ReLu),
              (input_size//3, ReLu),
              (input_size//3, ReLu),
              (7,ReLu)
            ]


class P4Agent(Agent):
  """
    Joueur de puissance 4
  """
  name = "Power 4 player"
  def __init__(self, id: int =None):
    super().__init__(init_NN=True, description=DESCRIPTION, id=id, sim=P4Simulator)

  def __str__(self):
    return self.__repr__()
