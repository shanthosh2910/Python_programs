def reverse(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev

print(reverse("shanthosh"))
