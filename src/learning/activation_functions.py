import numpy as np


def Sigmoid(vec: np.ndarray) -> np.ndarray:
    return 1/(1+np.exp(-vec))


def ReLu(vec: np.ndarray) -> np.ndarray:
    return np.maximum(0, vec)
