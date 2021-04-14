import numpy as np
from typing import Callable
from dataclasses import dataclass, field

Activation_Function = Callable[[np.ndarray], np.ndarray]

@dataclass
class Connection_Layer:
  input_size          : int
  output_size         : int
  activation_function : Activation_Function
  weight_matrix       : np.ndarray = field(init=False)
  bias_vector         : np.ndarray = field(init=False)

  def init_data(self) -> None:
    self.weight_matrix = np.random.normal(size=(self.output_size, self.input_size))
    self.bias_vector   = np.random.normal(size=self.output_size)

  def eval_forward(self, input_vec : np.ndarray) -> np.ndarray:
    neurons = self.weight_matrix.dot(input_vec)
    neurons += self.bias_vector
    return self.activation_function(neurons)

  def mutate(self, mutation_force : float) -> None:
    gaussian_bias_noise = np.random.normal(0, 1, self.output_size) * mutation_force
    self.bias_vector += gaussian_bias_noise
    weight_gaussian_noise = np.random.normal(0, 1, size =(self.output_size,self.input_size)) * mutation_force
    self.weight_matrix += weight_gaussian_noise

