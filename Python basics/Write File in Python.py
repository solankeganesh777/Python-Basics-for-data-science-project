#File Handling in Python

#Writing File
with open('/resources/data/Example2.txt',"w") as wfile:
    wfile.write("This is first line written")
    wfile.write("This is second line written")
    
#check if file is written
with open('/resources/data/Example2.txt',"r") as rfile:
    print(rfile.read())
    
#By setting the mode argument to append a you can append a new line
with open('/resources/data/Example2.txt',"a") as wf:
    wf.write("This is appended line")
with open('/resources/data/Example2.txt',"r") as rf:
    print(rf.read())
    
print('\n')
#Write a list to text file
family=['ganesh','mangesh','balasheb','vaishali']
print(family)

with open('/resources/data/Example3.txt',"w") as wrfl:
    for i in family:
        wrfl.write(i)
with open('/resources/data/Example3.txt',"r") as rfl:
    print(rfl.read())
    
print('\n')
#Copy a file
with open('/resources/data/Example2.txt',"r") as re:
    with open('/resources/data/Example3.txt',"w") as wr:
        for line in re:
            wr.write(line)
with open('/resources/data/Example3.txt',"r") as ro:
    print(ro.read())

    
