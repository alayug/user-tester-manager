#!/usr/bin/python
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import tkinter.ttk
from constants.mainConstants import *
from constants.insertTaskConstants import append
from validators.insertTaskValidator import *
from validators.insertUserValidator import *
from services.emailService import send_email
from services.dataService import *

# WORK IN PROGRESS - FIGURE OUT HOW TO COMPLETE THIS MULTI INPUT DIALOG BOX
class SimpleDialog():
    
    def __init__(self):
        super().__init__()
        # self allow the variable to be used anywhere in the class
        self.output1 = ""
        self.output2 = ""
        self.initUI()
        
    def initUI(self):
        window = Toplevel()
        lbl1 = Label(window, text="Input 1", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=10)

        self.entry1 = Entry(window, textvariable=self.output1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        lbl2 = Label(window, text="Input 2", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=10)

        self.entry2 = Entry(window)
        self.entry2.pack(fill=X, padx=5, expand=True)


        # Command tells the form what to do when the button is clicked
        btn = Button(window, text="Submit", command=self.onSubmit)
        btn.pack(padx=5, pady=10)

    def onSubmit(self):

        self.output1 = self.entry1.get()
        self.output2 = self.entry2.get()
        user_input = (self.output1, self.output2)
        print("user input", user_input)
        self.window.destroy()

#
# Callbacks for 
#
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
    message = ""

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
        # reset message to empty string so it wont trigger popup dialog
        message = ""
        # execute insert_user function. Retrieving the entry data by invoking get() on the variables
        insert_user([[firstName.get(), lastName.get(), emailAddress.get(), phoneNumber.get(), selectedInsertUserDropDownTask.get()]], 'a')
        # Clear all input fields for Add User
        clearInsertUserEntries()
        # Update Users Treeview with the most recently added data
        updateUsersTreeView()
    if message != "":
        messagebox.showinfo(title=None, message=message)

def insertTask():
    # Prompt a popup to ask for user's input for the task name
    taskNameInput = simpledialog.askstring(title="Add New Task", prompt="Enter the task name: ", initialvalue="")
    # Validate task name, and returns empty string if no errors
    taskNameValidatorMessage = taskNameValidator(taskNameInput)
    # If taskNameValidatorMessage is not empty string, throw a alert box for customer
    if taskNameValidatorMessage !="":
        messagebox.showinfo(title=None, message=taskNameValidatorMessage)
    else:
        # Get the most recent task id number and add 1 to create next task id
        nextTaskId = int(get_last_task_id()) + 1
        newTaskList = [nextTaskId, taskNameInput]
        # execute insert_task function, appending the newTaskList
        insert_task([newTaskList], append)
        # Update the Add User task dropdown
        updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu)
        # Update the Tasks treeview with added task
        updateTasksTreeView()

def deleteTask():
    # If no task has been selected from dropdown, throw a message
    if selectedDropDownDeleteTask.get() == "Select a task":
        messagebox.showinfo(title=None, message="You must select a task to delete!")
    else:
        # Gets current string of selected drop down delete task
        selectedDeleteTaskString = selectedDropDownDeleteTask.get()
        # Split the string by ' to get the string value of the task id
        stringTaskId = selectedDeleteTaskString.split("'")
        # Execute delete_task with int by converting string value of task id to int
        delete_task(int(stringTaskId[1]))
        updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu)
        updateTasksTreeView()

def deleteUser(emailFromSelectedItemInTreeView):
    if emailFromSelectedItemInTreeView == "": 
        messagebox.showinfo(title=None, message="Please select a user to delete!")
    else:
        # execute insert_user function. Retrieving the entry data by invoking get() on the variables
        delete_user(emailFromSelectedItemInTreeView)    
    # Update Users treeview with updated data from csv
    updateUsersTreeView()

# Function to clear all Insert User Entries
def clearInsertUserEntries():
    firstName.set("")
    lastName.set("")
    emailAddress.set("")
    phoneNumber.set("")
    selectedInsertUserDropDownTask.set("Select One")

class InsertUser: 
    def __init__(self,master) :
        ###### USER UI #######
        # Create all labels required for users.csv, using grid for organization
        insertUserTitle = Label(bottomFrame, text = ADD_USER, anchor=CENTER, font=tkFont.Font(size=16)).grid(row = 0,column = 1)
        firstNameLabel = Label(bottomFrame, text = FIRST_NAME).grid(row = 1,column = 0)
        lastNameLabel = Label(bottomFrame, text = LAST_NAME).grid(row = 2,column = 0)
        emailAddressLabel = Label(bottomFrame, text = EMAIL_ADDRESS).grid(row = 3,column = 0)
        phoneNumberLabel = Label(bottomFrame, text = PHONE_NUMBER).grid(row = 4,column = 0)
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
        Button(bottomFrame ,text=ADD_USER, command=insertUser, bg='SteelBlue4',fg='Snow').grid(row=6,column=1)
    

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

# Function to update User Treeview with newest data from csv
def insertUserDetailsIntoTreeView():
    index = 0

    # Creates a row for each item in get_user_details result list
    for user in get_user_details():
        usersTreeview.insert(parent='', index=index, iid=index, text='', values=(user[0], user[1], user[2], user[3], user[4]))
        index +=1

# Function to update Task Treeview with newest data from csv
def insertTaskDetailsIntoTreeView():
    index = 0

    # Creates a row for each item in get_user_details result list
    for task in get_task_details():
        tasksTreeview.insert(parent='', index=index, iid=index, text='', values=(task[0], task[1]))
        index +=1
        
# Function to trigger the custom multiple input dialog popup - IN PROGRESS
def showDialog():
    popup = SimpleDialog()
    

# CH example of how to manipulate a row that got a 2x click
def edit_task(event, *args):

        tview = event.widget # the TreeView widget on which we 2x clicked a row on
        row_id = event.widget.focus() # row id that was 2x clicked on
        values = event.widget.item(row_id)["values"] # the list of values in a row
 
        # popup dialog to task for the new task name to replace the selected one
        newTaskName = simpledialog.askstring("Edit Task Name", "Please enter the new task name:", initialvalue=values[1])

        # showDialog() // customer multi input  popup - IN PROGRESSS

        # show message alert box if and prevent update if field does not pass validation
        if(newTaskName.isspace() == True or newTaskName == ""):
            messagebox.showinfo(title=None, message="You must enter a task name!")
        else:
            # call update_task with current task Id and user inputted task name
            update_task(values[0], newTaskName)
            # update Tasks treeview with newest data from csv
            updateTasksTreeView()
            # update Add User's task dropdown with newest data
            updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu)

def edit_user(event, *args):

        tview = event.widget # the TreeView widget on which we 2x clicked a row on
        row_id = event.widget.focus() # row id that was 2x clicked on
        values = event.widget.item(row_id)["values"] # the list of values in a row
 
        # popup dialog to task for the new task name to replace the selected one
        newEmail = simpledialog.askstring("Edit User", "Please enter the email address:", initialvalue=values[2])
      
        # showDialog() // customer multi input  popup - IN PROGRESSS

        # display message box if validation does not pass and prevents update
        if(newEmail.isspace() == True or newEmail == ""):
            messagebox.showinfo(title=None, message="You must enter a email address!")
        elif(emailValidator(newEmail) != ""):
            messagebox.showinfo(title=None, message="Please enter a valid email address!")
        else:
            # if validation passes, call update_user with user's input
            update_user(values[2],newEmail)
            # update Users treeview with newest data from csv
            updateUsersTreeView()

        
class TreeView :
    def __init__(self, master):
        ####### SELECTION FIELD #########
        
        usersTreeview['columns']=(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE_NUMBER, TASK_NAME)
        usersTreeview.column('#0', width=0, stretch=NO)
        usersTreeview.column(FIRST_NAME, anchor='w', width=80)
        usersTreeview.column(LAST_NAME, anchor='w', width=80)
        usersTreeview.column(EMAIL_ADDRESS, anchor='w', width=120)
        usersTreeview.column(PHONE_NUMBER, anchor='w', width=100)
        usersTreeview.column(TASK_NAME, anchor='w', width=80)

        usersTreeview.heading('#0', text='', anchor='w')
        usersTreeview.heading(FIRST_NAME, text=FIRST_NAME, anchor='w')
        usersTreeview.heading(LAST_NAME, text=LAST_NAME, anchor='w')
        usersTreeview.heading(EMAIL_ADDRESS, text=EMAIL_ADDRESS, anchor='w')
        usersTreeview.heading(PHONE_NUMBER, text=PHONE_NUMBER, anchor='w')
        usersTreeview.heading(TASK_NAME, text=TASK_NAME, anchor='w')

        insertUserDetailsIntoTreeView()

        tasksTreeview['columns']=(TASK_ID, TASK_NAME)
        tasksTreeview.column('#0', width=0, stretch=NO)
        tasksTreeview.column(TASK_ID, anchor='w', width=80)
        tasksTreeview.column(TASK_NAME, anchor='w', width=200)

        tasksTreeview.heading('#0', text='', anchor='w')
        tasksTreeview.heading(TASK_ID, text=TASK_ID, anchor='w')
        tasksTreeview.heading(TASK_NAME, text=TASK_NAME, anchor='w')

        insertTaskDetailsIntoTreeView()

        # CH callback for left mouse button double click on a row of this treeview widget
        tasksTreeview.bind("<Double-1>", edit_task)
        usersTreeview.bind("<Double-1>", edit_user)

        def deleteUserThroughTreeview():
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

        def deleteTaskThroughTreeview():
            # Gets selected item index
            selectedItem = tasksTreeview.selection()
            if tasksTreeview.item(selectedItem)['values']=="" :
                messagebox.showinfo(title=None, message="Please select a task to delete.")
            else:
                answer = messagebox.askyesno(title='Delete Task Confirmation',
                    message='Are you sure that you want to delete the task?')
                if answer:
                    # Using index, get the item and then the value at index 2 which equals to emailAddress
                    taskIdFromSelectedItemInTreeView = tasksTreeview.item(selectedItem)['values'][0]
                    # Delete user from users.csv
                    delete_task(taskIdFromSelectedItemInTreeView)
                    updateTasksTreeView()
                    updateInsertUserTaskOptionMenu(insertUserTaskOptionMenu)
                    
     
        def email():
            # Gets currently selected item's data
            selectedItem = usersTreeview.selection()
            # Retrieves password from password field
            passwordValue = password.get()
            if passwordValue == "":
                message = "Please enter the password below before using the email service."
            # Prompt user to select a item in treeview if none is selected
            elif usersTreeview.item(selectedItem)['values']=="" :
                message="Please select a user to email." 
            else: 
                firstNameFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][0]
                emailFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][2]
                taskNameFromSelectedItemInTreeView = usersTreeview.item(selectedItem)['values'][4]
                dateToCompleteBy = simpledialog.askstring(title = "Complete task by...", prompt = "Please enter the date you want the user to complete the task by:", initialvalue="")
                timeToCompleteBy = simpledialog.askstring(title = "Complete task by...", prompt = "Please enter the time you want the user to complete the task by:", initialvalue="")
                if(dateToCompleteBy == ""):
                    message = "Please enter a date the user must complete their task by."
                elif(timeToCompleteBy == ""):
                    message = "Please enter a time the user must complete their task by."
                else:
                    additionalDetails = simpledialog.askstring(title = "Additional Details", prompt = "Additional details for the user (optional)", initialvalue="N/A")
                    send_email(emailFromSelectedItemInTreeView, passwordValue, firstNameFromSelectedItemInTreeView, taskNameFromSelectedItemInTreeView,dateToCompleteBy, timeToCompleteBy, additionalDetails)
                    message = "Email Sent!"
            messagebox.showinfo(title="Email Service", message=message)
        
        def displayUsersTreeview(): 
            usersTreeview.pack()
            deleteUserButton.pack()
            emailPasswordLabel.pack()
            emailPasswordEntry.pack()
            sendEmailButton.pack()
        
        def hideUsersTreeview():
            usersTreeview.pack_forget()
            deleteUserButton.pack_forget()            
            emailPasswordLabel.pack_forget()
            emailPasswordEntry.pack_forget()
            sendEmailButton.pack_forget()

        def displayTasksTreeview():
            tasksTreeview.pack()
            addTaskButton.pack()
            deleteTaskButton.pack()
        
        def hideTasksTreeview():
            tasksTreeview.pack_forget()
            addTaskButton.pack_forget()
            deleteTaskButton.pack_forget()

        def displayUsersButtonAction():
            hideTasksTreeview()
            displayUsersTreeview()

        def displayTasksButtonAction():
            hideUsersTreeview()
            displayTasksTreeview()

        deleteUserButton = Button(topFrame ,text="Delete User", command=deleteUserThroughTreeview)
        deleteUserButton.configure(bg='light coral')
        # Create all labels and entries button required for Users Treeview
        emailPasswordLabel = Label(topFrame, text = "Password for Email")
        emailPasswordEntry = Entry(topFrame, textvariable = password)
        sendEmailButton = Button(topFrame ,text="Email User", command=email)
        sendEmailButton.configure(bg='SteelBlue4',fg='Snow')

        # Create button to add task
        addTaskButton = Button(topFrame ,text="Add Task", command=insertTask)
        addTaskButton.configure(bg='SteelBlue4',fg='Snow')
        # Create button to delete task
        deleteTaskButton = Button(topFrame ,text="Delete Task", command=deleteTaskThroughTreeview)
        deleteTaskButton.configure(bg='light coral')

        displayUsersTreeviewButton = Button(topFrame ,text="Display Users", command=displayUsersButtonAction)
        displayUsersTreeviewButton.configure(bg='SteelBlue4',fg='Snow')
        displayTasksTreeviewButton = Button(topFrame ,text="Display Tasks", command=displayTasksButtonAction)
        displayTasksTreeviewButton.configure(bg='SteelBlue4',fg='Snow')

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
usersTreeview = tkinter.ttk.Treeview(topFrame, selectmode="browse")
tasksTreeview = tkinter.ttk.Treeview(topFrame, selectmode="browse")

# Create all variables required for insertUsers
firstName = StringVar()
lastName = StringVar()
emailAddress = StringVar()
phoneNumber = StringVar()
selectedInsertUserDropDownTask = StringVar(root)
selectedTaskTreeviewItem = StringVar()

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
insertUser = InsertUser(root)

#this will run the mainloop.
root.mainloop()