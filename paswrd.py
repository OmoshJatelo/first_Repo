def reset_pswd():
    print("seems like you have forgotten your password\n You neeed to reset it\n")
    new_pswd1=input("please enter your new passwrd:\n")
    new_pswd2=input("confirm your  new password ")
    while new_pswd1!=new_pswd2:
        print("password mismatch")
        new_pswd1=input("please enter your new passwrd: ")
        new_pswd2=input("confirm your  new password: ")
    print(f"You have successfully created your new password:{new_pswd2}")
    file=open("myFile","w")
    file.write(new_pswd2)
    file.close()
    pswd=open("myFile","r")
    pswd=pswd.read().strip()
    




file=open("myFile","w")
file.write("jatelo")
file.close()
pswd=open("myFile","r")
pswd=pswd.read().strip()
#print(pswd.read())


attempts=1

user_pswd=input("please enter your password\n:")
while user_pswd !=pswd and attempts<3:
    print("incorrect password, please try again")
    user_pswd=input("please enter your password:")
    
    attempts +=1
reset_pswd()   
            






