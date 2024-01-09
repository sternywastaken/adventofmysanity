from pathlib import Path

def solution():
	input_values = Path('input.txt').read_text().splitlines()
	total = 0
	score = 0
	win_nums = []
	your_nums = []
	for line in input_values:
		card, nums = line.split(':')
		win_nums.append(nums.split(" | ")[0])
		your_nums.append(nums.split(" | ")[1])

	for i in range(len(win_nums)):
		winning = []
		for num in win_nums[i].split():
			if num in your_nums[i].split():
				winning.append(num)
		print(winning)
		print()

		if len(winning) > 2:
			score = 2 ** (len(winning) - 1)
			print(score)
			total += score
		if len(winning) <= 2:
			score = len(winning)
			print(score)
			total += score


	print(total)


def solution2():
	cards = {}
	win_nums = []
	your_nums = []
	input_values = Path('input.txt').read_text().splitlines()
	for line in input_values:
		card, nums = line.split(':')
		cards[card] = 0
		win_nums.append(nums.split(" | ")[0])
		your_nums.append(nums.split(" | ")[1])
	print(cards)

	for i in range(len(win_nums)):
		winning = []
		for num in win_nums[i].split():
			if num in your_nums[i].split():
				winning.append(num)
		print(winning)
		print()
	


solution2()