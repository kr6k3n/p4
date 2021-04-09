from learning.agent import Agent

from p4sim import PowerSim

input_size = 7*6

SHAPE = [input_size,
         input_size//2,
         input_size//2,
         input_size//2,
         input_size//2,
         input_size//4,
         input_size//4,
         7]


class P4player(Agent):
  """
    Joueur de puissance 4
  """
  name = "Power 4 player"
  def __init__(self, id : int = None) -> None:
    super().__init__(init_NN=True, SHAPE=SHAPE, id=id, sim=PowerSim)

  def __str__(self):
    return self.__repr__()
