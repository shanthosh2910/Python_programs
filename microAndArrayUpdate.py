# Input: 
# First line consists of a single integer, T, denoting the number of test cases. 
# First line of each test case consists of two space separated integers denoting N and K. 
# Second line of each test case consists of N space separated integers denoting the array A. 

# Output:
# For each test case, print the minimum time in which all array elements will become greater than or equal to K. Print a new line after each test case. 

# SAMPLE INPUT
# 2
# 3 4
# 1 2 5
# 3 2
# 2 5 5

# SAMPLE OUTPUT
# 3
# 0


i = int(input())
while(i > 0):
    n,k = map(int, input().split(' '))
    minimum = min(map(int, input().split(' ')))
    if minimum < k:
        print(k - minimum)
    else:
        print(0)
    i -= 1