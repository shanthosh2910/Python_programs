def is_int(x):
    if round(x) - x == 0:
        return True
    else:
        return False

number = float(input("Number:"))
if is_int(number):
    print("is int")
else:
    print("not int")
