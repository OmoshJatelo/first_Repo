text="jatelo  is  an  aspiring    software  developer, s  trong man  jatelo 234 074"

#searching for patterns 

import re
find=re.search(r"jatelo",text)
if find:
    print("pattern found")

#matching patterns
matched=re.match(r"jatelo",text)
if matched:
    print("the pattern matched")


#finding all the instances of the pattern in the string
found=re.findall(r"jatelo",text) 
if found:
    print(found)


#substituting patterns in strings
new_text=re.sub(r"jatelo","omosh",text) 
print(new_text)

#replacing multiple spaces with a single space
replaced=re.sub(r"\s+"," ",text)
print(replaced)

#spliting text in a string . it splits the string based 
# on the specified patttern and returns a list
my_text="python, javascript, C++, html, CSS"
my_list=re.split(r",\s*",my_text)
print(my_list)


#extracting numbers in strings
numbers=re.findall(r"\d+",text)
if numbers:
    print(numbers)



    #validating email addressses
email="omoshjatelo35@gmail.com" 
email_format=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(email_format,email):
    print("the email adddress is valid") 
else:
    print(" sorry, the email address is invalid")      


