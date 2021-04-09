from typing import List, Any
from abc import abstractclassmethod, abstractproperty, ABC

class Simulator(ABC):
  winner : Any
  state : Any
  @abstractclassmethod
  def act(self, action) -> bool: # type: ignore
    """returns True if next turn can be played"""
    pass
  @abstractproperty
  def serialized_state(self) -> List[int]: # type: ignore
    pass
