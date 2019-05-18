import re


text = " 01-25-2019  11-06-1900 "

#         ( \1 ) ( \2 ) (   \3   )
pat = r"\b(\d\d)-(\d\d)-(\d\d\d\d)\b"
repl = r"\2/\1/\3"

# text = " 25/01/2019  06/11/1900 "
res = re.findall(pat, text)
print(res)
text2 = re.sub(pat, repl, text)
print(text2)