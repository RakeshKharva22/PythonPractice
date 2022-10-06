
"""
marks = 1000

a = marks/0
print(a)


try:
    a = int(input("Enter No."))
    r = a/0
    print(a)
except:
    print("Exception Caught")


from builtins import int

while True:
    try:
        n = int(input("Enter No. "))
        n = int(n)
        break
    except Exception:
        print("Invalid Input")
    finally:
        print("Finally Called")
print("Bye")

"""

try:
    #a=0
    print(a)
except NameError:
    print("Variable a is not defined")
except:
    print("something else")
else:
    print("Hello user")
finally:
    print("Finally block")
