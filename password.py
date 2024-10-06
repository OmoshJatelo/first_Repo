

def login():

    attempts=1
    password =input("please enter your password to log in ")
    while password != "jatelo" :
        
        while attempts < 2:
            print("oops! wrong password, please try again")
            password = input("enter your password to log in")
            attempts+=1
        print("seems like you forgot your password\nyou need to reset it") 
        break 
        

    print("loading, please wait") 



def resetPassword():
    password1=input(" please enter your new preferred password : ")
    password2=input("confirm your new password : ") 

    while password1!=password2 :
        print("password mismatch,try again")
        password1=input("create a password that you will remember easily : ")
        password2=input("confirm your password : ")
    print(f"you have successfuly created your new password: {password2}") 
    print("be sure to remember your password")




resetPassword()