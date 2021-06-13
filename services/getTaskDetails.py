import csv

def get_task_details():
    # Create list to store the csv data
    taskList = []

    # opens csv file
    with open(r'C:\bench\user-tester-manager\database\tasks.csv', 'r') as f:
        # csv reader will each line of data in the csv file
        reader = csv.reader(f)
        # for each row in the csv file, append to taskList
        for row in reader:
            taskList.append(row)
  
    return taskList