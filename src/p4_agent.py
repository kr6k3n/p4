from src.learning.neural_net import ReLu
from .learning.agent import Agent

from .p4_simulator import P4Simulator

input_size = 7*6

SHAPE = [input_size,
         input_size//2,
         input_size//2,
         input_size//2,
         input_size//2,
         input_size//4,
         input_size//4,
         7]


class P4Agent(Agent):
  """
    Joueur de puissance 4
  """
  name = "Power 4 player"
  def __init__(self, id: int =None):
    super().__init__(init_NN=True, SHAPE=SHAPE, activation_function=ReLu, id=id, sim=P4Simulator)

  def __str__(self):
    return self.__repr__()
