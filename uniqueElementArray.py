#  to find unique element in a array
#  the array should contain only one uique element
#  the array should contain only doublets

array = [12,12,11,11,13,45,45]
result = array[0]
for i in range(1,len(array)):
    result = result ^ array[i]
print(result)