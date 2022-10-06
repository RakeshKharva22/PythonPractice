class Person:
    fname=""
    lname=""
    email=""

    def __init__(self,fname,lname,email):
        print("Constructor Called ")
        self.fname=fname
        self.lname=lname
        self.email=email

    def showDetails(self):
        print("FName ",self.fname)
        print("LName ",self.lname)
        print("Email ",self.email)

fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
email = input("Enter Email: ")

p = Person(fname,lname,email)
p.showDetails()
