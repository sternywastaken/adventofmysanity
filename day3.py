from pathlib import Path
import re
import itertools

# create two lists of alternating lines, index 0, 2, 4 and index 1, 3, 5 and so on

def solution():
	part_numbers = []
	special = []
	nums = [str(x) for x in range(10)]
	input_values = Path('input.txt').read_text().splitlines()
	for line in input_values:
		for char in line:
			if char not in nums and char != '.':
				special.append(char)

	currnext = []
	for index, char in enumerate(input_values):
		if index + 1 < 140:
			lst = []
			lst.append(input_values[index])
			lst.append(input_values[index + 1])
			currnext.append(lst)
		else:
			break
	for index, l in enumerate(input_values):
		#print(l)
		num = re.findall(r"[+@_!#$%^&*()<>?/\|}{~:]\d+", l)
		num_ = re.findall(r"\d+[+@_!#$%^&*()<>?/\|}{~:]", l)
		#print(num + num_)
		# if len(num) and len(num_) > 0:
		# 	part_numbers += num[0][1]
		# 	part_numbers += num_[0][0]
		part_numbers += num + num_
	#print(part_numbers)

	first = []
	second = []
	for index, group in enumerate(currnext):
		if index + 1 > len(currnext):
			break
		else:
			for line, next_ in zip(group[0], group[1]):
				#print(line + next_)
				first.append(line)
				second.append(next_)
				#print(line, next_)
	
	for index, (f, s) in enumerate(zip(first, second)):
		if index + 1 < len(first):
			if f.isdigit() and second[index - 1] in special or second[index + 1] in special or second[index] in special:
				#print(f, s)
				if f.isdigit():
					part_numbers.append(f)

	print(currnext)
	print(input_values)

	for curline, nextline in currnext:
		pass
	# for index, group in enumerate(currnext):
	# 	nums = []
	# 	syms = []
	# 	for index, line in enumerate(group[0]):
	# 		dig = re.findall(r"\d+", line)
	# 		if len(dig) > 0:
	# 			nums.append(dig[0])
	# 	print(group[1])
	# 	print(nums)
	# 	for char, num in zip(group[1], group[0]):
	# 		number = ''
	# 		if char in special and group[1].index(char) + 1 == group[0].index(num) or group[1].index(char) == group[0].index(num):
	# 			number += num
	# 	print(number)

	#print(part_numbers)

solution()