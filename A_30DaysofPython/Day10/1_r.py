# Reading content from a file
file = open("sample.txt", "r")  # 'r' means read mode
content = file.read()
print(content)
file.close()
