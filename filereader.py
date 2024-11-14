file=open("jatelo.py")
lineNum=1
for line in file:
    
    if 'choice' in line:
          print(f"line {lineNum}: {line}")
    lineNum+=1


