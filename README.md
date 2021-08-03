# User Tester Manager
User Testing Manager is a tool that helps simplify the user testing management process.  Admin can add, manage, delete, and notify user testers about their testing sessions. It stores user tester's information such as their name, email, and contact number to send email reminders to user testers about the testing information such as time, date, and testing method. 


# Getting started
Python - 3.8 was used to compile and run the project. Feel free to download and use the latest version here https://www.python.org/downloads/  
GitBash - Will be needed to clone the repo and also commit changes.
Microsoft Visual Studios (optional) - A free to use IDE with great Python extensions. Feel free to use the IDE of your choice. 
Powershell (optional) - used to run scripts to execute your code. I used this but feel free to use any other way you'd like to execute the main.py file.

# Running the App
Open Windows Powershell and go into the directory in which you cloned the repo.

Copy and paste the following command into your Powershell:  
>& "{path-to-your-user-directory}/AppData/Local/Microsoft/WindowsApps/python3.9.exe" {path-to-cloned-repo}/user-tester-manager/main.py

If working properly, you should see the screen below:  
![image](https://user-images.githubusercontent.com/84653735/127938798-e137fb22-fe97-4e1d-b5ac-9e0c26faf2aa.png)

You are all ready to use the application!

# Technical Diagram
Below is the architecture for the application  
![image](https://user-images.githubusercontent.com/84653735/127946626-8f9b970f-2d5c-422d-86f6-1c35fa4110f6.png)

Overview of each component... 

**main.py** - This will consist of the UI and the starting point of your code execution to get the app running. (Refer to **Running the App** above).  
This component will have all the classes to create the UI such as the Treeview, Entry, and Labels. It will also hold all the button action functions that will trigger a call to the dataService.py file. All the modules used in this file are from Python's tkinter module.

**dataService.py** - This is the middleware that will retrieve, insert, update, and delete our data from the csv files. The function uses Python's csv module for all data modification.

**users.csv** - a csv file that will store all data associated with the user. It consists of first name, last name, email, phone number, and task name.

**tasks.csv** - a csv file that will store all data associated with a task. It consists of a unique task id and task name.  

**emailService.py** - this function will send a email to the user using Python's smtplib and Google's Gmail smtp server. A password is required to use the email service so please find the appropriate owner.

# Bugs and issues found during development
1. **RESOLVED** Do not rename emailService.py to email.py, there is a known bug in which the code will not recognize and execute the email functionality. 
2. **RESOLVED** User was able to select multiple fields in the Treeview. Set the Treeview with selectmode="browse". 
3. **IN PROGRESS** Creating a customer multi input popup dialog. Bug currently associated is that closing the dialog will close out the whole application.

*If you have any questions, feel free to email me at layugaliana@gmail.com*
