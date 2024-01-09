import re
from pathlib import Path
from collections import defaultdict

#12 red cubes, 13 green cubes, and 14 blue cubes
#create a dictionary of 13 green, 12 reds, 14 blues and compare their values to the input values
def solution():
	inputs = Path("input.txt").read_text().splitlines()
	ans_one = 0
	ans_two = 0

	for games in inputs:
		temp = defaultdict(int)
		possible = True
		id_, game = games.split(":")
		line = game.split(";")
		for groups in line:
			group = groups.split(',')
			for event in group:
				num, col = event.split()
				temp[col] = max(int(num), temp[col])
				if int(num) > {"red": 12, "green": 13, "blue": 14}.get(col):
					possible = False
		if possible:
			ans_one += int(id_.split()[1])
		power = 1
		for value in temp.values():
			power *= value
		ans_two += power

	print(ans_one)
	print(ans_two)


solution()