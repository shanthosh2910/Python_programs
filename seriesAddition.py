# 1+2+3+4+.....n can be done with the formula n(n+1)/2
n = int(input())
print(n * (n+1) / 2)

# sum of all numbers that are divisible by 3 or 5 upto n
# sum of numbers divisible by 3 can be identified by 3*n(n+1)/2 similarly for divisible by 5, 5*n(n+1)/2. To find the range divide n/3 , n/5, n/15
# but some numbers repeat for both 3 and 5 that are divisible by 15 . So lets subtract the sum of numbers divisible by 15

threeRange = n//3
fiveRange = n//5
fifteenRange = n//15
print((3 * threeRange * (threeRange + 1)) / 2 + ( 5 * fiveRange * (fiveRange + 1)) / 2 - ( 15 * fifteenRange * (fifteenRange + 1)) / 2)
