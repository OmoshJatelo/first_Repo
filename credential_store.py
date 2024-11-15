#create a class which will be used as a blue print for creating a store for credentials
class Credentials:
    def __init__(self,title,userName,password):
        self.title=title
        self.username=userName
        self.password=password


    #create a fnction for retrieving the credentials
    def getCred(self):
        cred =f"\ntitle:{self.title}\n User Name: {self.username}\nPassword:{self.password}"
        return cred
    
#input the credentials
cred1=Credentials("sodel","jatelo","#Omo2Teloja")
cred2=Credentials("students portal","Omosh calvo","@Demoshjatelo")

#print(cred1.getCred())
#print(cred2.getCred())

#store the credentials in a list
credstore=[]
credstore.append(cred1)
credstore.append(cred2)

#create a function that searches for the credentials
def search():
    query=input("enter your search term\n")
    for cred in credstore:
        if cred.title==query:
            print(cred.getCred())

search()            