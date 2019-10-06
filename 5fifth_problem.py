#!/usr/bin/env python3

# 4fourth_problem.py
# Calculate frequencies of words in a text


def for_sorting(e):
	return e[1]


def count_words(text):
	text = text.split()
	list_of_tuples = []

	for index in range(len(text)):
		count = text.count(text[index])
		if not (text[index], count) in list_of_tuples:
			list_of_tuples.append((text[index], count))
	list_of_tuples.sort(reverse=True, key=for_sorting)

	return list_of_tuples


print(count_words("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum."""))



