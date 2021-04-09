import enum
from typing import List, Union
from .learning.simulator import Simulator

class Player(enum.Enum):
  X = "X"
  O = "O"
  none = None

class P4Simulator(Simulator):
  def __init__(self):
    self.state : list = [[0]*7 for l in range(6)]
    self.turn  = "X"
    self.winner = None

  def __repr__(self):
    representation = "  P4 Sim:\n"
    for l in range(5, -1, -1):
      for c in range(0, 7):
        representation += " "
        if self.state[l][c] == 0:
          representation += "  | "
        elif self.state[l][c] == 1:
          representation += "O | "
        else:
          representation += "X | "
      representation += "\n"
    representation += "\n"
    return representation

  @property
  def next_turn(self) -> str:
    return "X" if self.turn == "O" else "X"

  def illegal_move(self, c) -> bool:
    return (self.state[5][c] != 0)

  def play(self, c: int) -> None:
    l = 0
    while self.state[l][c] != 0:
      l += 1
    self.state[l][c] = self.turn
    self.turn = "X" if self.turn == "O" else "X"

  def horiz(self, j: str, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l][c+i] != j:
        return False
    return True

  def vert(self, j: str, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l+i][c] != j:
        return False
    return True

  def diag1(self, j: str, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l+i][c+i] != j:
        return False
    return True

  def diag2(self, j: str, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l+i][c-i] != j:
        return False
    return True
  
  def get_winner(self) -> Union[str, None] :
    for player in ["X", "O"]:
      for l in range(6):
          for c in range(7):
              if c < 4 and self.horiz(player, l, c):
                return player
              if l < 3 and self.vert(player, l, c):
                return player
              if c < 4 and l < 3 and self.diag1(player, l, c):
                  return player
              if l < 3 and c > 2 and self.diag2(player, l, c):
                return player
    return None

  def draw(self) -> bool:
    for i in range(7):
      if self.state[5][i] == 0:
        return False
    return True

  def act(self, column) -> bool:
    """returns True if next turn can be played"""
    if self.illegal_move(column):
      self.winner = self.next_turn
      return False
    self.play(column)
    winner = self.get_winner()
    if winner != Player.none:
      self.winner = winner
      return False
    elif self.draw():
      self.winner = None
      return False
    return True

  @property
  def serialized_state(self) -> List[int]:
    serialized = list()
    for i in range(6):
      for j in range(7):
        serialized.append(self.state[i][j])
    return serialized
  
