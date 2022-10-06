from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("400x400")
root.title("My Tkinter First Example")
root.resizable(width=False,height=False)

#For_Labels
l_id = Label(root,text="ID")
l_id.place(x=50,y=80)

l_fname = Label(root,text="First Name")
l_fname.place(x=50,y=130)

l_lname = Label(root,text="Last Name")
l_lname.place(x=50,y=180)

l_email= Label(root,text="Email")
l_email.place(x=50,y=230)

l_mobile = Label(root,text="Mobile")
l_mobile.place(x=50,y=280)

#For_TextBoxes
e_id =Entry(root)
e_id.place(x=150,y=80)

e_fname=Entry(root)
e_fname.place(x=150,y=130)

e_lname=Entry(root)
e_lname.place(x=150,y=180)

e_email=Entry(root)
e_email.place(x=150,y=230)

e_mobile = Entry(root)
e_mobile.place(x=150,y=280)


#For_Buttons
insert = Button(root,text="INSERT", bg="black",fg="white",font=("Arial",10))
insert.place(x=50,y=330)

search = Button(root,text="SEARCH", bg="black",fg="white",font=("Arial",10))
search.place(x=120,y=330)

update = Button(root,text="UPDATE", bg="black",fg="white",font=("Arial",10))
update.place(x=200,y=330)

delete = Button(root,text="DELETE",bg="black",fg="white",font=("Arial",10))
delete.place(x=280,y=330)



