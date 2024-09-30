hotelMenu={"Ugali":"40" ,"Beef":"120", "Rice":"45", "beans":"30"}

print("Hey there! Welcome to Jatelo enterprise; your hotel of choice. Feel welcome and enjoy your best delicacies")

name=input("what is your name")

print(f"Hi {name}, here is a list of what we offer, feel free to make your best selection")

print(hotelMenu.items())
for attempts in range(10):
    choice=input("what would you like to eat")
    if choice in hotelMenu:
        print("please procced to take a seat, your food will be ready in a moment")
        break
    else:
        print("your selection is not in our menu, please try again")

    #choice=input("your selection is not in the menu, kindly make another selection")
#rint(" please proceed to take a seat, your meal will be ready in a moment")