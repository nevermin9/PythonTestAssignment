#!/usr/bin/env python3

# 3third_problem.py
# Check if a given string is palindrome


def is_palindrome(s):
	return s == s[::-1]


print(is_palindrome('eebbee'))
