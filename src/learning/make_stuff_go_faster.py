import fastrand
from multiprocessing import Pool
from tqdm import tqdm
from random import getrandbits

PROCESSES = 6


def r_number() -> float: 
	value = fastrand.pcg32() / int(2**32)
	return -value if bool(getrandbits(1)) else value


def fastmap(function, iterable, display_progress=False, progress_message="") -> list:
	with Pool(processes=PROCESSES) as p:
		max_ = len(iterable)
		if display_progress:
			with tqdm(total=max_) as pbar:
				result = list()
				for res in p.imap(func=function, iterable=iterable):
					pbar.update()
					result.append(res)
				return result
		else:
			return list(p.map(func=function, iterable=iterable))


#test
if __name__ == '__main__':
	def double(x):
		return x*2
	print(list(fastmap(double, range(10))))
