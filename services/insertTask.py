
import csv
from typing import List

# Takes in a list of task
def insert_task(newTaskList):
    print(newTaskList)
    # Insert new row in tasks.csv with task name, using 'a' to append the data
    with open(r'C:\bench\user-tester-manager\database\tasks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # for each task in the list, append to csv
        for task in newTaskList:
            writer.writerow(task)
