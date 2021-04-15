from src import P4Pool, save_pool_to_disk, restore_pool_from_disk
import os

from functools import wraps
from time import time


from config import training_config

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:{} took: {} sec'.format(f.__name__, te-ts))
        return result
    return wrap


def main():

	t_pool = restore_pool_from_disk(name=training_config["POOL_NAME"],
																	pool_folder_path=training_config["FOLDER_PATH"])
	if t_pool is None:
		t_pool = P4Pool(population_size=int(training_config["POPULATION_SIZE"]), 
										name=training_config["POOL_NAME"])
	@timing
	def execute_epoch():
		t_pool.epoch(demo_rate=training_config["DEMO_RATE"], debug=False)

	for epoch in range(training_config["EPOCHS"]):
		execute_epoch()
		if epoch % training_config["REDUCE_RATE"] == 0:
			for agent in t_pool.population:
				agent.NN.reduce_parameters()
		if epoch % training_config["SAVE_RATE"] == 0 :
			save_pool_to_disk(t_pool=t_pool, pool_folder_path=training_config["FOLDER_PATH"])
main()
