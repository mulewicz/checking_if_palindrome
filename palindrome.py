# -*- coding: utf-8 -*-
"""
@author: mulewicz
"""
word = input("enter a word: ")

for i in range(len(word)//2):
    if word[i] != word[len(word) - 1 - i]:
        print('it is not a palindrome')
        break
    else:
        print("it is a palindrome")
        break
