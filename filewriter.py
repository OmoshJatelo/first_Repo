file=open("myFile", "w")
file.write("\nthis is a file witten by Jatelo\n Jtelo is an intellect of colosus\n do you want to know more about Jatelo\n")
file.close()

lineNum=1
try:
    f=open("myFile","r")
    for line in f:
        if "Jatelo" in line:
            print((f"line {lineNum}: {line}"))
        lineNum+=1  
except FileNotFoundError:
    print("such file does not exist in didrectry")          