from .neural_net import Neural_Network

class Agent:
  """
    Classe de base pour un agent 
  """
  name = "None"
  def __init__(self,
               init_NN: bool=True,
               SHAPE:   List[int] = None,
               id:      int = None,
               sim :  Simulator=None):
    if init_NN:
      self.NN: Neural_Network = Neural_Network(SHAPE)
    else:
      self.NN: Neural_Network = None
    if not id is None:
      self.id = id
    self.sim = sim
    self.sim_instance = None
    score : float = None

  
  def get_action(self, input_vec) -> int:
    nn_output = self.NN.eval(input_vec)
    return nn_output.index(max(nn_output))

  def act(self) -> bool:
    current_state = self.sim_instance.serialized_state
    action = self.get_action(current_state)
    return self.sim_instance.act(action)
  
  def play_against_other(self, other) -> None:
    #create shared simulator
    new_sim = self.sim()
    other.sim, self.sim = new_sim, new_sim
    # play all game turns
    while not game_ended:
      game_ended = not self.act()
      if not game_ended:
        game_ended = not other.act()
    #assign score
    self.score += 1 if self.sim_instance.winner == "X" else (-1 if self.sim_instance.winner == "O" else 0.5)
    other.score += 1 if self.sim_instance.winner == "O" else (-1 if self.sim_instance.winner == "X" else 0.5)

