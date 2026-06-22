# file= open ('List .py')
# print(file .read())

# MODES
# W-- Write (create and a new overwrite)
# a--append mode (new file )
# r-- read Mode 
# x-- create mode (agar file already exist karta hai toh error aayega )

file =open ('gangadhar.txt','w')
file .write ("the countent is now overwiten.")
file.close()

file =open("gangadhar.'txt','a'")
file .write ("the countent is now overwiten.the content is added using a(append )mode")
file.close()
# print(file.read)


file =open ('gangadhar.txt','r')
for i in file:
    print(i)
file.close()

#with statement
with open('gangadhar.''txt''r') as file:
    print(file.read())


with open('gangadhar.''txt''r') as file:
    print(file.read())

with open('gangadhar.''txt''r') as file:
    file.write("countent overwriten")
    print("done")

#paths

from pathlib import path 
p=path ("shaktiman,txt")
if p.exists ():
    print("file exists")
else:
    print("file does not exist")


