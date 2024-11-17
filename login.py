
#initialization of the default passwword
default_password="jatelo"
passwordFile="password.txt"

#creation of a function to get the stored password
def get_stored_password():
    try:
        with open(passwordFile,"r") as file:
            return file.read().strip()
    except:
        with open(passwordFile,"w") as file:
            file.write(default_password)
        return default_password
    
#create a function that updates the default password
def update_password(new_password):
    with open(passwordFile,"w") as file:
        file.write(new_password)
    

#create a function that resets the password
def reset_password():
    new_password1=input("please enter your new preffered password: ")
    new_password2=input("confirm your new password: ")
    while new_password1!=new_password2:
        print("password mismatch")
        new_password1=input("please enter your new preffered password: ")
        new_password2=input("confirm your new password: ")
    update_password(new_password1)
    print(f"you have successfully created your new password:{new_password1}")


#create a function that enables user to attempt to log in
def login():
    for attempt in range(3):
        user_password=input("enter your password to log in:")
        if user_password==get_stored_password():
            print("log in successful")
            return True
        else:
            print("Sorry, you have entered a wrong password")

    return False


#create a function that obtains information about from numbers api website
def get_info():
    while True:
        try:
           num=int(input(" enter your favourite number to discover something interesting about it: "))
           break
        except ValueError:
            print("please enter a numerical number like 3, 27, etc")
       
    import requests
    info=requests.get(f"http://numbersapi.com/{num}")
       
    print(info.text)   

#the main program
if login():
    print("access granted")
    get_info()
else:
    reset_password()
    print("You can now proceed to log in") 
    login()
    get_info()   