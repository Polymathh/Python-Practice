# Adding more content instead of overwriting
file = open("sample.txt", "a")  # 'a' means append mode
file.write("\nThis is an extra line.")
file.close()
