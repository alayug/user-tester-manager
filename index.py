#!/usr/bin/python
from tkinter import *
from services.insertUser import insert_user
root = Tk()

# Create the size of the widget
root.geometry('500x500')

# Create all variables required for users.csv
firstName = StringVar()
lastName = StringVar()
emailAddress = StringVar()
phoneNumber = StringVar()
taskID = IntVar()

# Create all labels required for users.csv, using grid for organization
firstNameLabel = Label(root, text = "First Name").grid(row = 0,column = 0)
lastNameLabel = Label(root, text = "Last Name").grid(row = 1,column = 0)
emailAddressLabel = Label(root, text = "Email Address").grid(row = 2,column = 0)
phoneNumberLabel = Label(root, text = "Phone Number").grid(row = 3,column = 0)
taskIDLabel = Label(root, text = "Task ID").grid(row = 4,column = 0)

# Create all entries required for users.csv
firstNameEntry = Entry(root, textvariable = firstName).grid(row = 0,column = 1)
lastNameEntry = Entry(root, textvariable = lastName).grid(row = 1,column = 1)
emailAddressEntry = Entry(root, textvariable = emailAddress).grid(row = 2,column = 1)
phoneNumberEntry = Entry(root, textvariable = phoneNumber).grid(row = 3,column = 1)
taskIDEntry = Entry(root, textvariable = taskID).grid(row = 4,column = 1)


def insertUser():
    # execute insert_user function. Retrieving the entry data by invoking get() on the variables
   insert_user(firstName.get(), lastName.get(), emailAddress.get(), phoneNumber.get(), taskID.get())

# button to trigger function to insert user data
btn = Button(root ,text="Submit", command=insertUser).grid(row=5,column=0)


#this will run the mainloop.
root.mainloop()