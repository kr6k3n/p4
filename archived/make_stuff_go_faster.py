#import fastrand
from multiprocessing import Pool
from random import getrandbits, random
from typing import Optional
from tqdm import tqdm

PROCESSES = 1

POOL = None


def open_pool():
	global POOL
	POOL = Pool(processes=PROCESSES)

def close_pool():
	global POOL
	POOL.close()





def fastmap(function, iterable, display_progress=False, progress_message="") -> list:
	return list(map(function, iterable))
	# global POOL
	# max_ = len(iterable)
	# if display_progress:
	# 	with tqdm(total=max_) as pbar:
	# 		result = list()
	# 		for res in POOL.imap(func=function, iterable=iterable):
	# 			pbar.update()
	# 			result.append(res)
	# 		return result
	# else:
	# 	return POOL.map(func=function, iterable=iterable)



#test
if __name__ == '__main__':
	def double(x):
		return x*2
	print(list(fastmap(double, range(10))))
