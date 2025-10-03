'''
with statement modes: r (read, default), w (write, will overwrite existing contents),
                      a (append), x (create, if the file exists, return error)
'''
# with open("text.txt") as file:
#     content = file.read()
#     print(content)

# single line
# with open("text.txt", mode='a') as file:
#     file.write("Learning python is so fun.")

# multiple lines
# with open("text.txt", mode='w') as file:
#     file.write("Learning C is so fun. \nLearning Java is also fun as well.")

'''
os module: 
1. os.remove(filename)
    This will do os unlink functionality (disappear from your computer directly, cannot revert it back)
2. os.rmdir(dirname) 
    This statement only applies on empty directory (disappear from your computer directly, cannot revert it back)
3. os.walk(top, topdown=True, ...)
    This will travel through the folder, top is the dir you wanna explore,
    and return tuples (root, dirs, files)
    root: the current dir which you're walking
    dirs: a list, the dirs' name in the current dirs (not including the subdirs)
    files: a list, the files' name in the current dirs
'''

# os.remove("hello.txt")
# os.rmdir("new_dir")

import shutil
import os
for root, dirs, files in os.walk("."):
    print(f"The root is {root}.")
    print(f"Here contains dirs: {dirs}.")
    print(f"Here contains files: {files}.")


'''
shutil module:
1. shutil.rmtree(dirname) 
    This will remove all elements in the folder (cannot revert them back)
'''

# remove non-empty folder
shutil.rmtree("new_dir")
