#File Handling in Python

#Reading File

# Download Example file
!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt

#Read the txt file
example1 = "/resources/data/Example1.txt"
file1 = open(example1, "r")

#print path of file
print(file1.name)

print(file1.mode)

#Read the file
filecontent=file1.read()
print(filecontent)
type(filecontent)
file1.close()

print('\n')

#Better way to open the file using "with": This way automatically closes the file
with open(example1,"r") as file2:
    content=file2.read()
    print(content)
# Verify if the file is closed
print(file2.closed)

#Read only first 4 characters of file.If we call the method again, the next 4 characters are called
with open(example1,"r") as file3:
    print(file3.read(4))
    print(file3.read(7))
    print(file3.read(25))

#read one line of the file at a time using the method readline()
with open(example1,"r") as fi:
    print(fi.readline())
    print(fi.readline())

print('\n')

#Method redlines() to save text file as list
# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
    
print(FileasList[0])
print(FileasList[1])
