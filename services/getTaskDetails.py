import csv

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
