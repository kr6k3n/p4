import random
from src import P4Pool, intro

if __name__ == '__main__':
	#intro() #tete de shrek
	t_pool = P4Pool(population_size=10**3, name="Debug")
	for i in range(10):
		t_pool.epoch()


