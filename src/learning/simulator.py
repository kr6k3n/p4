from typing import List

class Simulator:
  def act(self, action) -> bool:
    """returns True if next turn can be played"""
    pass
  @property
  def serialized_state(self) -> List[int]:
    pass
