from .learning.trainpool import TrainPool
from .p4_agent import P4Agent


class P4Pool(TrainPool):
  def __init__(self, population_size: int,  name: str = "Unnammed") -> None:
      super().__init__(population_size, agent=P4Agent, name=name)