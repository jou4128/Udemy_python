import os

now_path = os.getcwd()
file_path = os.path.join(now_path, "IO", "text.txt")

'''
file = open(filename) will open a file and return a file object.
'''

file = open(file_path)
# print(file)

'''
file.read(n) read the file with n words (if there is no n, read full file) and return string
while finishing the read, there's a seek will record the end position of read function
'''
# print(file.read(10))
# print(file.read(10))

'''
file.seek(offset) can reset the record position e.g. file.seek(0) make the file be readed from scratch
'''
# print(file.read(5))
# file.seek(0)
# print(file.read(5))

'''
file.readlines() will return a list
file.readline() will read the file line by line
'''
# print(file.readlines())
# print(file.readline())
# print(file.readline())

'''file.close() close the process, if the program is large, that will fill up your memory'''
