

def login():
     
    defaultPassword=['jatelo']
    attempts=1
    password =input("\nplease enter your password to log in\n ")
    while password != defaultPassword[0]:
        
        while attempts < 3:
            print("oops! wrong password, please try again\n")
            password = input("enter your password to log in\n")
            attempts+=1
        print("seems like you forgot your password\nyou need to reset it\n") 
        
       #print("loading, please wait")        
        password1=input(" please enter your new preferred password : ")
        password2=input("confirm your new password : ") 

        while password1!=password2 :
            print("password mismatch,try again")
            password1=input("create a password that you will remember easily : ")
            password2=input("confirm your password : ")

        defaultPassword.clear()
        defaultPassword=defaultPassword.append(password2) 
        print(defaultPassword)  
        print(f"you have successfuly created your new password: {password2}") 
        print("be sure to remember your password")
        break
    
    print("welcome back")
    




login()



print("\nLife without fun can be very boring\n but did you know that with python youcn actually overcome boredom?\nwant to know how?\nlet me show you")
while True:
    try:
        num =int(input("Enter any number and discover something interesting:\n"))
        break
    except ValueError:
       print("please enter a numerical number only, like 2, 56, 101 etc")
       
    

import requests
response=requests.get(f"http://numbersapi.com/{num}")
print(response.text)