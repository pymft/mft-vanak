import re


text = """As a result
Many variations of these original 
forms of regular expressions were used in 
Unix[9] programs at Bell Labs """

pattern = "\W[aeiou]\w\W"

res = re.findall(pattern, text)
print(res)

