#RegEX (Regular Expressions) in python

import re


#print(dir(re))

name="ganesh solanke will become a best data scientist"
print(re.search("^ganesh.*scientist$",name))

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
print(x)

print("\n")
#1.findall():Returns a list containing all matches

txt="Ganesh is a good boy and will become a best data scientist soon"
print(re.findall("st",txt))

print("\n")
#2.Search(): searches the string for a match, and returns a Match object if there is a match,
#If there is more than one match, only the first occurrence of the match will be returned

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position:", x.start()) 

print("\n")
#3.Split():returns a list where the string has been split at each match

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 

print("\n")
#4.Sub(): replaces the matches with the text of your choice
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)    

