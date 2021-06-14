#!/usr/bin/python
from tkinter import *
import tkinter.ttk 
from constants.insertTask import append
from services.insertUser import insert_user
from services.insertTask import insert_task
from services.deleteTask import delete_task

root = Tk()

# Create the size of the widget
root.geometry('500x500')

# Create all variables required for insertUsers
firstName = StringVar()
lastName = StringVar()
emailAddress = StringVar()
phoneNumber = StringVar()
taskId = IntVar()

# Create all variables required for insertTask
id = IntVar()
taskName = StringVar()

# Create all variables required for deleteTask 
deleteTaskId = IntVar()

def insertUser():
    # execute insert_user function. Retrieving the entry data by invoking get() on the variables
   insert_user(firstName.get(), lastName.get(), emailAddress.get(), phoneNumber.get(), taskId.get())

def insertTask():
    newTaskList = [id.get(), taskName.get()]
    # execute insert_task function. Retrieving the entry data by invoking get() on the variables
    insert_task([newTaskList], append)

def deleteTask():
    # execute insert_task function. Retrieving the entry data by invoking get() on the variables
    print("inside delete task")
    delete_task(deleteTaskId.get())

###### USER UI #######
# Create all labels required for users.csv, using grid for organization
firstNameLabel = Label(root, text = "First Name").grid(row = 0,column = 0)
lastNameLabel = Label(root, text = "Last Name").grid(row = 1,column = 0)
emailAddressLabel = Label(root, text = "Email Address").grid(row = 2,column = 0)
phoneNumberLabel = Label(root, text = "Phone Number").grid(row = 3,column = 0)
taskIDLabel = Label(root, text = "Task Id").grid(row = 4,column = 0)

# Create all entries required for users.csv
firstNameEntry = Entry(root, textvariable = firstName).grid(row = 0,column = 1)
lastNameEntry = Entry(root, textvariable = lastName).grid(row = 1,column = 1)
emailAddressEntry = Entry(root, textvariable = emailAddress).grid(row = 2,column = 1)
phoneNumberEntry = Entry(root, textvariable = phoneNumber).grid(row = 3,column = 1)
taskIDEntry = Entry(root, textvariable = taskId).grid(row = 4,column = 1)

# button to trigger function to insert user data
Button(root ,text="Add User", command=insertUser).grid(row=5,column=1)

tkinter.ttk.Separator(root, orient=VERTICAL).grid( row=0, column = 6, rowspan=50, sticky='ns')


###### INSERT TASK UI #######
# Create all labels required for tasks.csv, using grid for organization
taskIdLabel = Label(root, text = "Task Id").grid(row = 0,column = 8)
taskNameLabel = Label(root, text = "Task Name").grid(row = 1,column = 8)

# Create all entries required for tasks.csv
taskIdEntry = Entry(root, textvariable = id).grid(row = 0,column = 9)
taskNameEntry = Entry(root, textvariable = taskName).grid(row = 1,column = 9)

# button to trigger function to add task data
Button(root ,text="Add Task", command=insertTask).grid(row=2,column=9)

###### DELETE TASK UI #######
# Create all labels required for tasks.csv, using grid for organization
deleteTaskLabel = Label(root, text = "Task Id").grid(row = 5,column = 8)

# Create all entries required for tasks.csv
deleteTaskEntry = Entry(root, textvariable = deleteTaskId).grid(row = 5,column = 9)

# button to trigger function to delete task data
Button(root ,text="Delete Task", command=deleteTask).grid(row=6,column=9)


#this will run the mainloop.
root.mainloop()