def censor(text, word):
    if word in text:
        text = text.replace(word, "*" * len(word))
    return text
print(censor("the","thesis"))
