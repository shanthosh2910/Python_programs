def anti_vowel(text):
    newtext = ''
    for c in text:
        if c not in "aeiouAEIOU":
            newtext += c
    return newtext
print(anti_vowel("shanthoshaAe"))
