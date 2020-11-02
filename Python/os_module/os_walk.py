import os

path= "/home/arraygen/Desktop/Akshata/Learning"
for (dirpath, dirnames, filenames) in os.walk(path):
    for files in [os.path.join(dirpath, file) for file in filenames]:
        print(files)

print("*"*20)
print("Avoid displaying hidden files")
for root, dirs, files in os.walk(path):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    print(files)
    print(dirs)