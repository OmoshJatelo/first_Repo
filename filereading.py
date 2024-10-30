file=open("jatelo.py")
#content=file.readline()
#print(content)
#lineNum=1
#for line in file:
    #print(f"line{lineNum}:{line}")
    #lineNum+=1


lineNum=1
for line in file:
    if "we" in line:
        print(f"line{lineNum}:{line}")
    lineNum+=1