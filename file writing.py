#file=open("list,py","r")  #opens the file in read mode, it is the default mode
#file=open("list,py","a") #opens the file in append mode
#file=open("list,py","w") #opens the file in write mode
#file=open("list,py","X") #creates a new file
#content=file.read()
#print(content)

#file=open("list,py","a")
#file.write("\n my file is now appended correctly\nit is so entertaining")
#file.close()
#f=open("list,py" ,"r")
#print(f.read())


file= open("list,py","a")
file.write("\nits splendid to see this menu\n its cool")
file.close()
try:
   file=open("list,py","r")
   print(file.read())
except FileNotFoundError:
   print("sorry, such file does not exist")


