import math
inp = int(input())
a = []
for i in range(0, inp):
    num = int(input())
    a.append(num)
for i in a:
    print(math.factorial(i))
