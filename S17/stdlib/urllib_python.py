import urllib.request

with urllib.request.urlopen("https://www.python.org") as fp:
    mybytes = fp.read()

print(type(mybytes))
text = mybytes.decode("utf-8")
print(type(text))
print(text)
# convert bytes to str python3