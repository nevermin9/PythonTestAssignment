#!/usr/bin/env python3

# 2second_problem.py
# Get unique items from a list


def get_unique_items(l):
	new_list = []
	for i in l:
		if i not in new_list:
			new_list.append(i)
	return new_list


print(get_unique_items([1, 3, 1, 4, 5, 3, 4, 5, 10]))


