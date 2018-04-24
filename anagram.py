# Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. 
# Any characters can be deleted from either of the strings.

# Input:
# 1
# cde
# abc

# Output:
# 4
# Anagram - Hackerearth


for iterate in range(0, int(input())):
    string1 = input()
    string2 = input()
    for letter in string1:
        if letter in string2:
            string1 = string1.replace(letter, '', 1)
            string2 = string2.replace(letter, '', 1)
    print(len(string1) + len(string2))
