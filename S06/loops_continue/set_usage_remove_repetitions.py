text = """Nothing can ever happen twice. 
In a consequence the sorry fact is. 
That we arrive here improvised 
and leave without the chance to practice
"""
# print(text)
words = text.split()
unique_words = set(words)
# print(len(words))
# print(len(unique_words))

for w in unique_words:
    print(words.count(w), w)