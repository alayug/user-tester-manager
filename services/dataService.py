import csv

# Takes in list with list of the following values - first_name,last_name,email_address,phone_number,task_id
def insert_user(newUserList, appendOrWrite):
    # Insert new row in users.csv with list, using 'a' to append the data
    with open(r'database\users.csv', appendOrWrite, newline='') as f:
        writer = csv.writer(f)
        # For each item in the newUserList, append to users.csv
        for user in newUserList:
            writer.writerow(user)

def delete_task(taskId):
    # get all the current tasks in csv
    currentTaskList = get_task_details()
    # list to store the new data that will write over the current tasks.csv file
    newTaskList = []

    for task in currentTaskList:
        # if the row (task[0] = taskId) in tasks.csv does not match the taskId parameter, add to newTaskList
        if int(task[0]) != taskId:
            newTaskList.append(task)
    
    # replace everything in current tasks.csv with newTaskList by passing in 'w' as second parameter
    insert_task(newTaskList,'w')

def delete_user(email):
    # get all the current users in users.csv
    currentUserList = get_user_details()
    # list to store the new data that will write over the current users.csv file
    newUserList = []

    for user in currentUserList:
        # if the row (users[2] = email) in users.csv does not match the email parameter, add to newUserList
        if str(user[2]) != str(email):
            newUserList.append(user)
    
    # replace everything in current users.csv with newUserList by passing in 'w' as second parameter
        insert_user(newUserList,'w')

def get_task_details():
    # Create list to store the csv data
    taskList = []

    # opens csv file, using 'r' for read
    with open(r'database\tasks.csv', 'r') as f:
        # csv reader will each line of data in the csv file
        reader = csv.reader(f)
        # for each row in the csv file, append to taskList
        for row in reader:
            taskList.append(row)
  
    return taskList

def get_task_detail_names():
    # Create list to store the csv data
    taskListNames = []

    # opens csv file, using 'r' for read
    with open(r'database\tasks.csv', 'r') as f:
        # csv reader will each line of data in the csv file
        reader = csv.reader(f)
        # for each row in the csv file, append to taskList
        for row in reader:
            taskListNames.append(row[1])
  
    return taskListNames

def get_last_task_id():
    # Get list of current tasks
    taskDetailsList = get_task_details()
    # Get last list item of taskDetailsList
    lastTaskInList = taskDetailsList[len(taskDetailsList) - 1]
    # Return the task id of the last item in the list
    return lastTaskInList[0]

def get_user_details():
    # Create list to store the csv data
    userDetailsList = []

    # opens csv file, using 'r' for read
    with open(r'database\users.csv', 'r') as f:
        # csv reader will each line of data in the csv file
        reader = csv.reader(f)
        # for each row in the csv file, append to userDetailsList
        for row in reader:
            userDetailsList.append(row)
  
    return userDetailsList

# Takes in a list of task, and writeOrAppend ('w' or 'a')
def insert_task(newTaskList, writeOrAppend):
    # open file tasks.csv and insert new row in with task id and name, using 'a' to append the data
    with open(r'database\tasks.csv', writeOrAppend, newline='') as f:
        writer = csv.writer(f)
        # for each task in the list, append to csv
        for task in newTaskList:
            writer.writerow(task)

