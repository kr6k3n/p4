from src import P4Pool
import os

def main():

	pool_folder_path = os.getcwd() + "/pool_saves"
	t_pool = P4Pool(population_size=int(80), name="Debug", restore=False, pool_folder_path=pool_folder_path)
	for i in range(10000):
		t_pool.epoch(demo_rate=1000, debug=False)
		# if i % 50 == 0:
	# 	print("saved epoch #", i)
	# 	t_pool.save(pool_folder_path=pool_folder_path)

if __name__ == '__main__':
	try:
		main()
	except:
		pass
