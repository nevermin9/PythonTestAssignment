#!/usr/bin/env python3

# 4fourth_problem.py
# Find three the largest items from a list


def get_3_largest(l):
	three_largest = []
	amount_of_items = 3

	if not l:
		return three_largest
	elif len(l) <= 3:
		return l
	else:
		for i in range(0, amount_of_items):
			largest = 0
			for item in range(len(l)):
				if largest < l[item]:
					largest = l[item]
			l.remove(largest)
			three_largest.append(largest)
		return three_largest


print(get_3_largest([3, 2, 1, 5, -1, 7, 3, 8]))
