# A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. 
# An alphabet is Dhananjay's Magical alphabet if its ASCII value is prime.

# Input format:
# First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.

# Output Format:
# For each test case, print Dhananjay's Magical Word in a new line.

# Input:
# 1
# 6
# AFREEN

# Output:
# CGSCCO

# Magical word  - Hacker earth

prime = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
testcase = int(input())
for _ in range(testcase):
    length = input()
    word = input()
    for letters in word:
        ascii = ord(letters)
        if ascii < 67:
            print(chr(67), end='')
        elif ascii > 89 and ascii <= 90:
            print(chr(89), end='')
        elif ascii > 113:
            print(chr(113), end='')
        elif ascii in prime:
            print(letters, end='')
        else:
            for cursor in range(1, 12):
                if ascii > prime[cursor-1] and ascii < prime[cursor]:
                    if prime[cursor] - ascii < ascii - prime[cursor-1]:
                        print(chr(prime[cursor]), end='')
                    else:
                        print(chr(prime[cursor-1]), end='')
    print()