import math

def ReLu(x: float) -> float:
	if (x > 0):
		return x
	return 0


def Sigmoid(x: float) -> float:
  return math.pow(math.exp(-x) + 1 , -1)