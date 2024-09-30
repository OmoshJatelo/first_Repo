def readfile (filename):
    f=open(filename)
    content= f.read()
    return content


def writefile(filename,content):
    content=str(content)
    file=open(filename, "w")
    file.write(content)
    file.close()

    
try:    
   num=int(readfile("list.txt"))
except ValueError:
   num=0
   num=int(num)
         
print(f"this file has been read {num} times")
num+=1
writefile("list.txt",num)

    



