from src import P4Pool
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

	pool_folder_path = os.getcwd() + "/pool_saves"
	t_pool = P4Pool(population_size=int(training_config["POPULATION_SIZE"]), name="Debug", restore=False, pool_folder_path=pool_folder_path)
	@timing
	def execute_epoch():
		t_pool.epoch(demo_rate=10, debug=training_config["DEMO_RATE"])

	for _ in range(training_config["EPOCHS"]):
		execute_epoch()
		# if i % 50 == 0:
	# 	print("saved epoch #", i)
	# 	t_pool.save(pool_folder_path=pool_folder_path)

main()
