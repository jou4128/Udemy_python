from sys import argv

file = open(argv[1])
content = file.read()
lines = content.split("\n")
line_count = len(lines) - 1

word_count = 0
letter_count = 0
for line in lines:
    word = line.split(" ")
    word_count += len(word)
    letter_count += len(line)

print(f"Line count is {line_count}")
print(f"Word count is {word_count}")
print(f"Letter count is {letter_count}")
