iteration = int(input())
t = []
n = []
r = []
sumValue = []
for i in range(0, iteration):
    t.append(int(input()))
    n.append(int(input()))
    r.append(int(input()))
    sumValue.append(t[i]/n[i])

for i in range(0, iteration):
    result=int(sumValue[i] * 10 ** r[i]) % 10
    print(result)
