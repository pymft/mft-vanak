text = "Nothing can ever happen twice. In a consequence the sorry fact is. "

words = text.split()

print(words)
print(len(words))

vowels = []
consonants = []
words_new = []

for w in words:
    if w[0].lower() in "aeiou":
        vowels.append(w)
    else:
        consonants.append(w)

print(vowels)
print(consonants)