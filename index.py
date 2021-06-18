#!/usr/bin/python
from services.getUserDetails import get_user_details
from tkinter import *
from tkinter import messagebox
import tkinter.ttk 
from constants.insertTask import append
from services.insertUser import insert_user
from services.insertTask import insert_task
from services.deleteTask import delete_task
from services.deleteUser import delete_user

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
    message = ""
    # Validation check on fields to ensure it is not empty
    if firstName.get() == "":
        message = "First Name can't be empty!"
    elif lastName.get() =="":
        message = "Last Name can't be empty!"
    elif emailAddress.get() =="":
        message = "Email Address can't be empty!"
    elif phoneNumber.get() =="":
        message = "Phone Number can't be empty!"
    elif taskId.get() =="":
        message = "Task Id can't be empty!"
    else:
    # execute insert_user function. Retrieving the entry data by invoking get() on the variables
        insert_user([[firstName.get(), lastName.get(), emailAddress.get(), phoneNumber.get(), taskId.get()]], 'a')
        message = "User was inserted successfully!"
    messagebox.showinfo(title=None, message=message)


def insertTask():
    newTaskList = [id.get(), taskName.get()]
    # execute insert_task function. Retrieving the entry data by invoking get() on the variables
    insert_task([newTaskList], append)
    messagebox.showinfo(title=None, message="Task was inserted successfully!")

def deleteTask():
    # execute insert_task function. Retrieving the entry data by invoking get() on the variables
    delete_task(deleteTaskId.get())
    messagebox.showinfo(title=None, message="Task was deleted successfully!")

def deleteUser(emailFromSelectedItemInTreeView):
    # execute insert_user function. Retrieving the entry data by invoking get() on the variables
    delete_user(emailFromSelectedItemInTreeView)
    messagebox.showinfo(title=None, message="User was deleted successfully!")

def getUserDetails():
    # execute get_user_detail
    userDetailsList = get_user_details()
    return userDetailsList

# Using Frame to group UI to two sections, top and bottom
topFrame= Frame(root)
topFrame.pack(side=TOP, fill=BOTH, expand=True)

bottomFrame= Frame(root)
bottomFrame.pack(side=BOTTOM, fill=BOTH)

class InsertUser: 
    def __init__(self,master) :
        ###### USER UI #######
        # Create all labels required for users.csv, using grid for organization
        firstNameLabel = Label(bottomFrame, text = "First Name").grid(row = 0,column = 0)
        lastNameLabel = Label(bottomFrame, text = "Last Name").grid(row = 1,column = 0)
        emailAddressLabel = Label(bottomFrame, text = "Email Address").grid(row = 2,column = 0)
        phoneNumberLabel = Label(bottomFrame, text = "Phone Number").grid(row = 3,column = 0)
        taskIDLabel = Label(bottomFrame, text = "Task Id").grid(row = 4,column = 0)

        # Create all entries required for users.csv
        firstNameEntry = Entry(bottomFrame, textvariable = firstName).grid(row = 0,column = 1)
        lastNameEntry = Entry(bottomFrame, textvariable = lastName).grid(row = 1,column = 1)
        emailAddressEntry = Entry(bottomFrame, textvariable = emailAddress).grid(row = 2,column = 1)
        phoneNumberEntry = Entry(bottomFrame, textvariable = phoneNumber).grid(row = 3,column = 1)
        taskIDEntry = Entry(bottomFrame, textvariable = taskId).grid(row = 4,column = 1)

        # button to trigger function to insert user data
        Button(bottomFrame ,text="Add User", command=insertUser).grid(row=5,column=1)

        tkinter.ttk.Separator(bottomFrame, orient=VERTICAL).grid( row=0, column = 6, rowspan=50, sticky='ns')


class InsertTask:
    def __init__(self, master):
        ###### INSERT TASK UI #######
        # Create all labels required for tasks.csv, using grid for organization
        taskIdLabel = Label(bottomFrame, text = "Task Id").grid(row = 0,column = 8)
        taskNameLabel = Label(bottomFrame, text = "Task Name").grid(row = 1,column = 8)

        # Create all entries required for tasks.csv
        taskIdEntry = Entry(bottomFrame, textvariable = id).grid(row = 0,column = 9)
        taskNameEntry = Entry(bottomFrame, textvariable = taskName).grid(row = 1,column = 9)

        # button to trigger function to add task data
        Button(bottomFrame ,text="Add Task", command=insertTask).grid(row=2,column=9)

        ###### DELETE TASK UI #######
        # Create all labels required for tasks.csv, using grid for organization
        deleteTaskLabel = Label(bottomFrame, text = "Task Id").grid(row = 5,column = 8)

        # Create all entries required for tasks.csv
        deleteTaskEntry = Entry(bottomFrame, textvariable = deleteTaskId).grid(row = 5,column = 9)

        # button to trigger function to delete task data
        Button(bottomFrame ,text="Delete Task", command=deleteTask).grid(row=6,column=9)


class TreeView :
    def __init__(self, master):
        ####### SELECTION FIELD #########
        tv = tkinter.ttk.Treeview(topFrame)
        tv['columns']=("First Name", "Last Name", "Email Address", "Phone Number", "Task Id")
        tv.column('#0', width=0, stretch=NO)
        tv.column("First Name", anchor=CENTER, width=80)
        tv.column("Last Name", anchor=CENTER, width=80)
        tv.column("Email Address", anchor=CENTER, width=100)
        tv.column("Phone Number", anchor=CENTER, width=80)
        tv.column("Task Id", anchor=CENTER, width=80)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading("First Name", text="First Name", anchor=CENTER)
        tv.heading("Last Name", text="Last Name", anchor=CENTER)
        tv.heading("Email Address", text="Email Address", anchor=CENTER)
        tv.heading("Phone Number", text="Phone Number", anchor=CENTER)
        tv.heading("Task Id", text="Task Id", anchor=CENTER)

        index = 0

        # Creates a row for each item in getUserDetails result list
        for user in getUserDetails():
            tv.insert(parent='', index=index, iid=index, text='', values=(user[0], user[1], user[2], user[3], user[4]))
            index +=1

        def delete():
            # Gets selected item index
            selectedItem = tv.selection()
            # Using index, get the item and then the value at index 2 which equals to emailAddress
            emailFromSelectedItemInTreeView = tv.item(selectedItem)['values'][2]
            # Delete user from users.csv
            deleteUser(emailFromSelectedItemInTreeView)
            # Delete row from TreeView
            tv.delete(selectedItem)
     
        def email():
            messagebox.showinfo(None, message="Email Sent!")

        deleteUserButton = Button(topFrame ,text="Delete", command=delete)
        sendEmailButton = Button(topFrame ,text="Email User", command=email)


        tv.pack()
        deleteUserButton.pack()
        sendEmailButton.pack()

treeView = TreeView(root)
insertTask = InsertTask(root)
insertUser = InsertUser(root)

#this will run the mainloop.
root.mainloop()