all:
	python main.py
time:
	python -m cProfile -s time main.py
