import os

try:
    os.mkdir("MyDirPractice")
    os.chdir("MyDirPractice")
    for a in range(5):
        os.mkdir("myDir"+ str(a))
except: print("Folder already exist!")

# try:
for b in os.listdir("MyDirPractice"):
    filen="ads"
    print(b)
    os.chdir(b)
    for c in range(10):
        open(filen+c+".txt", 'w')
    os.chdir('..')
    print (os.path.abspath(os.curdir))
# except: print("File already exist!")
