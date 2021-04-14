from typing import List, Any
import numpy as np
from abc import abstractclassmethod, abstractproperty, ABC

class Simulator(ABC):
  winner : Any
  state : Any
  @abstractclassmethod
  def act(self, action) -> bool: # type: ignore
    """returns True if next turn can be played"""
    pass
  @abstractclassmethod
  def serialized_state(self, player_id) -> np.ndarray: # type: ignore
    pass
