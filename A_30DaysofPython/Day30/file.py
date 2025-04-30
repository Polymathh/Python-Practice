fileName = input("Enter the file name (e.g, file.txt): ")

try:
    with open(fileName, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        chars = len(content)

        print(f"Lines: {len(lines)}")
        print(f'words: {len(words)}')
        print(f'characters: {chars}')

except FileNotFoundError:
    print("File not fount. Please check the name and try again.")