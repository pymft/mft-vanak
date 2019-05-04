f = open('C:\\Users\\210-Teacher\\PycharmProjects\\mft-vanak\\S11\\file_manipulation\\input.txt')
f = open(r"C:\Users\210-Teacher\PycharmProjects\mft-vanak\S11\file_manipulation\input.txt")
f = open("input.txt", mode="r")

text = f.read()
f.close()

print(text)

