# gets set of number as a string
# prints the occurence of numbers from 0 to 9 in the string
number = input()
count = 0
for i in range(0,10):
    for num in number:
        if i == int(num):
            count += 1
    print(i,count)
    count = 0