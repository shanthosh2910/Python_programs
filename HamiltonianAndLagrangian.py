# you want to find all the marks that are not smaller than those on its right side in the array.

# Input Format
# The first line of input will contain a single integer n denoting the number of students.
# The next line will contain n space separated integers representing the marks of students.

# Output Format
# Output all the integers separated in the array from left to right that are not smaller than those on its right side.

# SAMPLE INPUT:
# 6
# 16 17 4 3 5 2

#SAMPLE OUTPUT
# 17 5 2

n = input()
a = input().split()
v = []
x = 0
while a:
    y = int(a.pop())
    if y >= x:
        v += y,
        x = y
while v:
    print(v.pop(),end=' ')