#!/usr/bin/python
from constants.mainConstants import FIRST_NAME, LAST_NAME
from services.getTaskDetails import get_last_task_id, get_task_details, get_task_detail_names
from validators.insertTaskValidator import taskNameValidator
from validators.insertUserValidator import emailValidator, firstNameValidator, lastNameValidator, phoneNumberValidator
from services.emailService import send_email
from services.getUserDetails import get_user_details
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter.ttk 
from constants.insertTaskConstants import append
from services.insertUser import insert_user
from services.insertTask import insert_task
from services.deleteTask import delete_task
from services.deleteUser import delete_user


#
# Callbacks for 
#
def updateDeleteTaskOptionMenu(deleteTaskOptionMenu): 
    # Remove current delete task drop down
    deleteTaskOptionMenu.destroy()
    # Get newest list of task details
    taskDetailsList = get_task_details()
    
    # Create new delete task drop down
    deleteTaskOptionMenu = OptionMenu(bottomFrame, selectedDropDownDeleteTask, *taskDetailsList)
    # Set newest delete task drop down at the previous drop down's location
    deleteTaskOptionMenu.grid(row = 5,column = 9)
    selectedDropDownDeleteTask.set("Select a task")

def updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu): 
    # Remove current insert user task drop down
    insertUserTaskOptionMenu.destroy()
    # Get newest list of task details
    taskDetailsList = get_task_detail_names()
    
    # Create new insert user task drop down
    insertUserTaskOptionMenu = OptionMenu(bottomFrame, selectedInsertUserDropDownTask, *taskDetailsList)
    # Set newest insert user task drop down at the previous drop down's location
    insertUserTaskOptionMenu.grid(row = 5,column = 1)
    selectedInsertUserDropDownTask.set("Select One")

def insertUser():
    # Validates every field in insertUser to ensure it meets criteria
    firstNameValidatorMessage = firstNameValidator(firstName.get())
    lastNameValidatorMessage = lastNameValidator(lastName.get())
    emailAddressValidatorMessage = emailValidator(emailAddress.get())
    phoneNumberValidatorMessage = phoneNumberValidator(phoneNumber.get())

    # If any fields return a message indicating a regex violation, display the message in a messagebox
    if firstNameValidatorMessage != "":
        message = firstNameValidatorMessage
    elif lastNameValidatorMessage != "":
        message = lastNameValidatorMessage
    elif emailAddressValidatorMessage != "":
        message = emailAddressValidatorMessage
    elif phoneNumberValidatorMessage != "":
        message = phoneNumberValidatorMessage
    elif selectedInsertUserDropDownTask.get() =="Select One":
        message = "You must select a task from the task list!"
    else:
    # execute insert_user function. Retrieving the entry data by invoking get() on the variables
        insert_user([[firstName.get(), lastName.get(), emailAddress.get(), phoneNumber.get(), selectedInsertUserDropDownTask.get()]], 'a')
        message = "User was added successfully!"
    messagebox.showinfo(title=None, message=message)
    clearInsertUserEntries()
    updateUsersTreeView()

def insertTask():
    taskNameValidatorMessage = taskNameValidator(insertTaskName.get())
    # Validation check on fields to ensure it is not empty
    if taskNameValidatorMessage !="":
        message = taskNameValidatorMessage
    else:
        # Get the most recent task id number and add 1 to create next task id
        nextTaskId = int(get_last_task_id()) + 1
        newTaskList = [nextTaskId, insertTaskName.get()]
        # execute insert_task function. Retrieving the entry data by invoking get() on the variables
        insert_task([newTaskList], append)
        message = "Task added successfully!"
    messagebox.showinfo(title=None, message=message)
    clearInsertTaskEntry()
    updateUsersTreeView()
    updateDeleteTaskOptionMenu(deleteTaskOptionMenu)
    updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu)
    updateTasksTreeView()

def deleteTask():
    # If no task has been selected from dropdown, throw a message
    if selectedDropDownDeleteTask.get() == "Select a task":
        message = "You must select a task to delete!"
    else:
        # Gets current string of selected drop down delete task
        selectedDeleteTaskString = selectedDropDownDeleteTask.get()
        # Split the string by ' to get the string value of the task id
        stringTaskId = selectedDeleteTaskString.split("'")
        # Execute delete_task with int by converting string value of task id to int
        delete_task(int(stringTaskId[1]))
        message = "Task was deleted successfully!"
    messagebox.showinfo(title=None, message=message)
    updateDeleteTaskOptionMenu(deleteTaskOptionMenu)
    updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu)
    updateTasksTreeView()

def deleteUser(emailFromSelectedItemInTreeView):
    if emailFromSelectedItemInTreeView == "":
        message = "Please select a user to delete!"
    else:
        # execute insert_user function. Retrieving the entry data by invoking get() on the variables
        delete_user(emailFromSelectedItemInTreeView)
        message = "User was deleted successfully!"
    messagebox.showinfo(title=None, message=message)
    updateUsersTreeView()

# Returns a list of user details
def getUserDetails():
    userDetailsList = get_user_details()
    return userDetailsList

# Returns a list of task names
def getAllTaskNames():
    taskDetailNamesList = get_task_detail_names()
    return taskDetailNamesList

def clearInsertUserEntries():
    firstName.set("")
    lastName.set("")
    emailAddress.set("")
    phoneNumber.set("")
    selectedInsertUserDropDownTask.set("Select One")

def clearInsertTaskEntry():
    insertTaskName.set("")

class InsertUser: 
    def __init__(self,master) :
        ###### USER UI #######
        # Create all labels required for users.csv, using grid for organization
        insertUserTitle = Label(bottomFrame, text = "Add User", anchor=CENTER, font=tkFont.Font(size=16)).grid(row = 0,column = 1)
        firstNameLabel = Label(bottomFrame, text = FIRST_NAME).grid(row = 1,column = 0)
        lastNameLabel = Label(bottomFrame, text = LAST_NAME).grid(row = 2,column = 0)
        emailAddressLabel = Label(bottomFrame, text = "Email Address").grid(row = 3,column = 0)
        phoneNumberLabel = Label(bottomFrame, text = "Phone Number").grid(row = 4,column = 0)
        taskIDLabel = Label(bottomFrame, text = "Task").grid(row = 5,column = 0)

        # Create all entries required for users.csv
        firstNameEntry = Entry(bottomFrame, textvariable = firstName).grid(row = 1,column = 1)
        lastNameEntry = Entry(bottomFrame, textvariable = lastName).grid(row = 2,column = 1)
        emailAddressEntry = Entry(bottomFrame, textvariable = emailAddress).grid(row = 3,column = 1)
        phoneNumberEntry = Entry(bottomFrame, textvariable = phoneNumber).grid(row = 4,column = 1)

        # Set default value
        selectedInsertUserDropDownTask.set("Select One")
       
        insertUserTaskOptionMenu.grid(row = 5,column = 1)
        # button to trigger function to insert user data
        Button(bottomFrame ,text="Add User", command=insertUser).grid(row=6,column=1)

        tkinter.ttk.Separator(bottomFrame, orient=VERTICAL).grid( row=0, column = 6, rowspan=50, sticky='ns')

class InsertTask:
    def __init__(self, master):
        ###### INSERT TASK UI #######
        # Create all labels required for tasks.csv, using grid for organization
        addTaskTitle = Label(bottomFrame, text = "Add Task", font=tkFont.Font(size=16)).grid(row = 0,column = 9)
        taskNameLabel = Label(bottomFrame, text = "Task Name").grid(row = 1,column = 8)

        # Create all entries required for tasks.csv
        taskNameEntry = Entry(bottomFrame, textvariable = insertTaskName).grid(row = 1,column = 9)

        # button to trigger function to add task data
        Button(bottomFrame ,text="Add Task", command=insertTask).grid(row=2,column=9)

        ###### DELETE TASK UI #######
        # Get all tasks to populate
        
        deleteTaskTitle = Label(bottomFrame, text = "Delete Task", font=tkFont.Font(size=16)).grid(row = 4,column = 9)
        # Create all labels required for tasks.csv, using grid for organization
        deleteTaskLabel = Label(bottomFrame, text = "Task").grid(row = 5,column = 8)

        selectedDropDownDeleteTask.set("Select a task")
        # Set delete task drop down menu at certain grid location
        deleteTaskOptionMenu.grid(row = 5,column = 9)

        # button to trigger function to delete task data
        Button(bottomFrame ,text="Delete Task", command=deleteTask).grid(row=6,column=9)

def updateUsersTreeView():
    # Deletes all contents of treeview
    usersTreeview.delete(*usersTreeview.get_children())
    # Repopulate treeview with newest user details
    insertUserDetailsIntoTreeView()

def updateTasksTreeView():
    # Deletes all contents of treeview
    tasksTreeview.delete(*tasksTreeview.get_children())
    # Repopulate treeview with newest task details
    insertTaskDetailsIntoTreeView()

def insertUserDetailsIntoTreeView():
    index = 0

    # Creates a row for each item in getUserDetails result list
    for user in getUserDetails():
        usersTreeview.insert(parent='', index=index, iid=index, text='', values=(user[0], user[1], user[2], user[3], user[4]))
        index +=1

def insertTaskDetailsIntoTreeView():
    index = 0

    # Creates a row for each item in getUserDetails result list
    for task in get_task_details():
        tasksTreeview.insert(parent='', index=index, iid=index, text='', values=(task[0], task[1]))
        index +=1

# CH example of how to manipulate a row that got a 2x click
def edit_task(event, *args):

        tview = event.widget # the TreeView widget on which we 2x clicked a row on
        row_id = event.widget.focus() # row id that was 2x clicked on
        values = event.widget.item(row_id)["values"] # the list of values in a row

        print(values) # show 2x clicked row content
 
        # Here you would pop up a dialog with text fields that show the current values
        # for this row and that can be edited. On OK, you would delete the current row
        # and re-create (insert) it with the new values from the dialog 

        # new_text = show_edit_dialog(values[1]) # assume we only want to edit the task name 
        new_text = "This is a user edited task name" # this is what we would get back from the dialog
        
        new_values = [values[0], new_text] # here I keep the old Task Id
        tview.delete(row_id) # delete current row and insert again with new values
        tview.insert("", row_id, values=new_values) # overwrite current row with modified values list


class TreeView :
    def __init__(self, master):
        ####### SELECTION FIELD #########
        
        usersTreeview['columns']=(FIRST_NAME, LAST_NAME, "Email Address", "Phone Number", "Task Name")
        usersTreeview.column('#0', width=0, stretch=NO)
        usersTreeview.column(FIRST_NAME, anchor=CENTER, width=80)
        usersTreeview.column(LAST_NAME, anchor=CENTER, width=80)
        usersTreeview.column("Email Address", anchor=CENTER, width=120)
        usersTreeview.column("Phone Number", anchor=CENTER, width=100)
        usersTreeview.column("Task Name", anchor=CENTER, width=80)

        usersTreeview.heading('#0', text='', anchor=CENTER)
        usersTreeview.heading(FIRST_NAME, text=FIRST_NAME, anchor=CENTER)
        usersTreeview.heading(LAST_NAME, text=LAST_NAME, anchor=CENTER)
        usersTreeview.heading("Email Address", text="Email Address", anchor=CENTER)
        usersTreeview.heading("Phone Number", text="Phone Number", anchor=CENTER)
        usersTreeview.heading("Task Name", text="Task Name", anchor=CENTER)

        insertUserDetailsIntoTreeView()

        tasksTreeview['columns']=("Task Id", "Task Name")
        tasksTreeview.column('#0', width=0, stretch=NO)
        tasksTreeview.column("Task Id", anchor=CENTER, width=80)
        tasksTreeview.column("Task Name", anchor=CENTER, width=200)

        tasksTreeview.heading('#0', text='', anchor=CENTER)
        tasksTreeview.heading("Task Id", text="Task Id", anchor=CENTER)
        tasksTreeview.heading("Task Name", text="Task Name", anchor=CENTER)

        insertTaskDetailsIntoTreeView()

        # CH callback for left mouse button double click on a row of this treeview widget
        tasksTreeview.bind("<Double-1>", edit_task)

        def delete():
            # Gets selected item index
            selectedItem = usersTreeview.selection()
            if usersTreeview.item(selectedItem)['values']=="" :
                messagebox.showinfo(title=None, message="Please select a user to delete.")
            else:
                answer = messagebox.askyesno(title='Delete User Confirmation',
                    message='Are you sure that you want to delete the user?')
                if answer:
                    # Using index, get the item and then the value at index 2 which equals to emailAddress
                    emailFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][2]
                    # Delete user from users.csv
                    deleteUser(emailFromSelectedItemInTreeView)
     
        def email():
            # Gets currently selected item's data
            selectedItem = usersTreeview.selection()
            # Retrieves password from password field
            passwordValue = password.get()
            if passwordValue == "":
                message = "Please enter the password below before using the email service."
            # Prompt user to select a item in treeview if none is selected
            elif usersTreeview.item(selectedItem)['values']=="" :
                message="Please select a user to delete." 
            else: 
                firstNameFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][0]
                emailFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][2]
                taskNameFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][4]
                send_email(emailFromSelectedItemInTreeView, passwordValue, firstNameFromSelectedItemInTreeView, taskNameFromSelectedItemInTreeView)
                message = "Email Sent!"
            messagebox.showinfo(title="Email Service", message=message)
        
        def displayUsersTreeview(): 
            usersTreeview.pack()
            deleteUserButton.pack()
            deleteTaskLabel.pack()
            deleteTaskEntry.pack()
            sendEmailButton.pack()
        
        def hideUsersTreeview():
            usersTreeview.pack_forget()
            deleteUserButton.pack_forget()            
            deleteTaskLabel.pack_forget()
            deleteTaskEntry.pack_forget()
            sendEmailButton.pack_forget()

        def displayTasksTreeview():
            tasksTreeview.pack()
        
        def hideTasksTreeview():
            tasksTreeview.pack_forget()

        def displayUsersButtonAction():
            hideTasksTreeview()
            displayUsersTreeview()

        def displayTasksButtonAction():
            hideUsersTreeview()
            displayTasksTreeview()

        deleteUserButton = Button(topFrame ,text="Delete User", command=delete)
        # Create all labels required for tasks.csv, using grid for organization
        deleteTaskLabel = Label(topFrame, text = "Password for Email")
        # Create all entries required for tasks.csv
        deleteTaskEntry = Entry(topFrame, textvariable = password)
        sendEmailButton = Button(topFrame ,text="Email User", command=email)



        displayUsersTreeviewButton = Button(topFrame ,text="Display Users", command=displayUsersButtonAction)
        displayTasksTreeviewButton = Button(topFrame ,text="Display Tasks", command=displayTasksButtonAction)

        displayUsersTreeviewButton.pack()
        displayTasksTreeviewButton.pack()
        displayUsersTreeview()        

#
# MAIN
#


root = Tk()

# Create the size of the widget
root.geometry('550x600')
root.title("User Tester Manager")

# Using Frame to group UI to two sections, top and bottom
topFrame= Frame(root)
topFrame.pack(side=TOP, fill=BOTH, expand=True)

bottomFrame= Frame(root)
bottomFrame.pack(side=BOTTOM, fill=BOTH)
bottomFrame.place(anchor="c", relx=.45, rely=.8)

# Create treeview (table) for users
usersTreeview = tkinter.ttk.Treeview(topFrame)
tasksTreeview = tkinter.ttk.Treeview(topFrame)

# Create all variables required for insertUsers
firstName = StringVar()
lastName = StringVar()
emailAddress = StringVar()
phoneNumber = StringVar()
selectedInsertUserDropDownTask = StringVar(root)

# Create all variables required for insertTask
insertTaskName = StringVar()

# Create all variables required for deleteTask 
selectedDropDownDeleteTask = StringVar()

# Message/Alert box message holder
message = ""

# Email from the selected item in treeview
emailFromSelectedItemInTreeView =""

# Password for email service
password = StringVar()

# Get list of all the tasks
taskDetailsList = get_task_details()
# Create delete task drop down menu
deleteTaskOptionMenu = OptionMenu(bottomFrame, selectedDropDownDeleteTask, *taskDetailsList)

# Get list of task names
taskNamesList = get_task_detail_names()
# Create default dropdown menu
insertUserTaskOptionMenu = OptionMenu(bottomFrame, selectedInsertUserDropDownTask, *taskNamesList)


# create Treeview widgets
treeView = TreeView(root)
insertTask = InsertTask(root)
insertUser = InsertUser(root)

#this will run the mainloop.
root.mainloop()