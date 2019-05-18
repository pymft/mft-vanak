text = """As a result
Many variations of these original 
forms of regular expressions were used in 
Unix[9] programs at Bell Labs """

pattern = ""

index = text.find(pattern, 0)
print(index)
index = text.find(pattern, index+1)
print(index)
index = text.find(pattern, index+1)
print(index)