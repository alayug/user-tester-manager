# User Tester Manager
User Testing Manager is a tool that helps simplify the user testing management process.  Admin can add, manage, delete, and notify user testers about their testing sessions. It stores user tester's information such as their name, email, and contact number to send email reminders to user testers about the testing information such as time, date, and testing method. 


# Getting started
**Python (Required)** - 3.8 was used to compile and run the project. Feel free to download and use the latest version here https://www.python.org/downloads/  
**GitBash (Required)** - Will be needed to clone the repo and also commit changes.
**Microsoft Visual Studios (optional)** - A free to use IDE with great Python extensions. Feel free to use the IDE of your choice.  
**Powershell (optional)** - used to run scripts to execute your code. I used this but feel free to use any other way you'd like to execute the main.py file.

# Running the App
## If using Visual Studios
Open the project in Visual Studios and open the main.py file. Afterwards you can simply click on the Play button on the top right.  
![image](https://user-images.githubusercontent.com/84653735/127949010-07896bfc-9794-449a-b0d1-6ccb16a1eb49.png)

## If not using Visual Studios
Open Windows Powershell and go into the directory in which you cloned the repo.

Copy and paste the following command into your Powershell:  
>& "{path-to-your-user-directory}/AppData/Local/Microsoft/WindowsApps/python3.9.exe" {path-to-cloned-repo}/user-tester-manager/main.py

## If working properly, you should see the screen below:  
![image](https://user-images.githubusercontent.com/84653735/127938798-e137fb22-fe97-4e1d-b5ac-9e0c26faf2aa.png)

## Switching Views (User & Task View)
In the application, you can toogle between user view and list view using the two blue buttons above called "Display User" & "Display Task"

## Adding a User
To add a user, fill out the add user fields (first name, last name, email, phone) and select a task from the dropdown.

## Deleting a User
To delete a user, select a user from the list and click the "delete user" button. A confirmation pop-up will appear to confirm your action.

## Editing a User information (email only)
Currently, the edit only is available to the user's email address. To edit the user's email address, select the user and double click the email address. A pop-up will appear that lets you edit the email in the field.

## Sending Email Reminders
To send an email reminder to a user, select a user, type in the password, and click the "Email User" button. A pop-up asking for more information will appear (Time, Date, and Additional Info). Fill out the information and a confirmation pop-up will appear once the email has been sent.

## Adding a Task
To add a task, go to the Task View (make sure you select "Display Task" button if you don't see the task list). Click "Add Task" button and a pop-up will appear asking for the task name. Fill out the field and hit "OK". The task should now also be available in the dropdown if you're adding a user.

## Deleting a Task
To delete a task, select a task from the list and click the "Delete Task" button. A confirmation pop-up will appear to confirm your action.

You are all ready to use the application!

# Technical Diagram
Below is the architecture for the application  
![image](https://user-images.githubusercontent.com/84653735/127946626-8f9b970f-2d5c-422d-86f6-1c35fa4110f6.png)

Overview of each component... 

**main.py** - This will consist of the UI and the starting point of your code execution to get the app running. (Refer to **Running the App** above).  
This component will have all the classes to create the UI such as the Treeview, Buttons, Dropdown, Popup Dialogs, Entry, and Labels. It will also hold all the button action functions that will trigger a call to the dataService.py file. All the modules used in this file are from Python's tkinter module.

**dataService.py** - This is the middleware that will retrieve, insert, update, and delete our data from the csv files. The function uses Python's csv module for all data modification.

**users.csv** - a csv file that will store all data associated with the user. It consists of first name, last name, email, phone number, and task name.

**tasks.csv** - a csv file that will store all data associated with a task. It consists of a unique task id and task name.  

**emailService.py** - this function will send a email to the user using Python's smtplib and Google's Gmail smtp server. A password is required to use the email service so please find the appropriate owner.

# Code Structure and Setup
![image](https://user-images.githubusercontent.com/84653735/128588114-434f7bfb-2159-4da4-9af5-187918c2085b.png)  
The image above displays the project structure.

**__pycache__** - Things that are cached by Python during development. We put this in the .gitignore so you will not see this file on Github.  
**.vscode** - Settings for Visual Studios, please feel free to use them if you are using Visual Studio.  
**constants** - This is the directory to store common strings that are used throughout the code. By putting them in a file, you can easily refactor and rename anything if they happen to change in the future.  
**database** - This directory stores all the "data" for the application. The data will be stored in a csv format in the csv files, which are just comma seperated values.  
**docs** - Directory will consists of simple docs that may be helpful to users or developers.  
**services** - This folder consists of the middleware that will allow communication between the UI and the backend (csv). It holds the code to modify data and email users.  
**tests** - Folder that will store all the test for the code.  
**validators** - Directory that holds all the validators for each input field in the UI to ensure they pass before allowing the data to be modified.  
**.gitignore** - This file holds all the files that you do not want to be committed to Github. Such good files to add in here would be passwords or things common to only your local machine such as cache.  
**main.py** - This is the starting point and the place where you will execute Python to start up the application.  
**README.md** - This is what you are currently reading. This provides users with a good starting point and details about your application.  
**run_unit_tests.py** - Executing this will run all the tests you have. You will have to import your test files into this file.

# Modules
Every module used in this application came from Python when it was installed so no additional need to use pip for additional modules! 

# Bugs and issues found during development
1. **RESOLVED** Do not rename emailService.py to email.py, there is a known bug in which the code will not recognize and execute the email functionality. 
2. **RESOLVED** User was able to select multiple fields in the Treeview. Set the Treeview with selectmode="browse". 
3. **IN PROGRESS** Creating a customer multi input popup dialog. Bug currently associated is that closing the dialog will close out the whole application.

*If you have any questions, feel free to email me at layugaliana@gmail.com*
