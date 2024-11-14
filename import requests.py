
print("\nLife without fun can be very boring\n but did you know that with python youcn actually overcome boredom?\nwant to know how?\nlet me show you")
while True:
    try:
        num =int(input("Enter any number and discover something interesting:"))
        break
    except ValueError:
       print("please enter a numerical number only, like 2, 56, 101 etc")
       
    

import requests
response=requests.get(f"http://numbersapi.com/{num}")
print(response.text)
