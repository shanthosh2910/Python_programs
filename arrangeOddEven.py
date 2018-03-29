# arrange the even digits first and odd digits second of the given number vice versa
# First input is option and next the value If the option is 0 - odd digits first 1 - even digits first
# input : 0 89745
# output : 97584

value = input().split(' ')
odd = ''
even = ''
for i in value[1]:
    p = int(i)
    if p % 2 == 0:
        even = even+i
    else:
        odd = odd+i
if value[0] == '0':
    print(odd+even)
else:
    print(even+odd)