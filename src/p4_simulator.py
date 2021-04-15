from dataclasses import dataclass, field
from .learning.simulator import Simulator

from typing import List, Union
import enum

import numpy as np

class Player(enum.Enum):
  X = "X"
  O = "O"
  none = None

@dataclass
class P4Simulator(Simulator):
  state: List[List[int]] = field(default_factory=(lambda: [[0]*7 for _ in range(6)]))
  turn  = "X"
  winner = None

  def __repr__(self):
    representation = str()
    for l in range(5, -1, -1):
      for c in range(0, 7):
        representation += " |"
        if self.state[l][c] == 0:
          representation += " |"
        elif self.state[l][c] == 1:
          representation += "X|"
        else:
          representation += "O|" # O est l'état défini par -1
      representation += "\n"
    representation += "\n"
    return representation

  @property
  def next_turn(self) -> str:
    return "X" if self.turn == "O" else "O"

  def illegal_move(self, c) -> bool:
    return (self.state[5][c] != 0)

  def play(self, c: int) -> None:
    l = 0
    while self.state[l][c] != 0:
      l += 1
    self.state[l][c] = 1 if self.turn == "O" else -1
    self.turn = "X" if self.turn == "O" else "O"

  def horiz(self, j: int, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l][c+i] != j:
        return False
    return True

  def vert(self, j: int, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l+i][c] != j:
        return False
    return True

  def diag1(self, j: int, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l+i][c+i] != j:
        return False
    return True

  def diag2(self, j: int, l: int, c: int) -> bool:
    for i in range(4):
      if self.state[l+i][c-i] != j:
        return False
    return True
  
  def get_winner(self) -> Union[str, None] :
    for player in ["X", "O"]:
      player_val = 1 if player == "X" else -1
      for l in range(6):
          for c in range(7):
              if c < 4 and self.horiz(player_val, l, c):
                return player
              if l < 3 and self.vert(player_val, l, c):
                return player
              if c < 4 and l < 3 and self.diag1(player_val, l, c):
                  return player
              if l < 3 and c > 2 and self.diag2(player_val, l, c):
                return player
    return None

  def draw(self) -> bool:
    for i in range(7):
      if self.state[5][i] == 0:
        return False
    return True

  def act(self, column) -> bool:
    """returns True if game ended"""
    if self.illegal_move(column):
      self.winner = self.next_turn
      return True
    self.play(column)
    winner = self.get_winner()
    if not winner is None:
      self.winner = winner
      return True
    elif self.draw():
      self.winner = None
      return True
    return False

  def serialized_state(self, player_id) -> np.ndarray:
    serialized = list()
    for i in range(6):
      for j in range(7):
        val = self.state[i][j] * (1 if player_id == "X" else -1) #inverser les valeurs selon le joueur
        serialized.append(val)
    return np.array(serialized)
  
