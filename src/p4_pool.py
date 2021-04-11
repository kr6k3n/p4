from .learning.trainpool import TrainPool
from .p4_agent import P4Agent


class P4Pool(TrainPool):
  def __init__(self, population_size: int,  name: str = "Unnammed",restore=False, pool_folder_path=None) -> None:
      super().__init__(population_size, 
                       agent=P4Agent, 
                       name=name, 
                       restore=restore, 
                       pool_folder_path=pool_folder_path)
