
import csv

# Takes in a list of task
def insert_task(newTaskList, writeOrAppend):
    # Insert new row in tasks.csv with task name, using 'a' to append the data
    with open(r'C:\bench\user-tester-manager\database\tasks.csv', writeOrAppend, newline='') as f:
        writer = csv.writer(f)
        # for each task in the list, append to csv
        for task in newTaskList:
            writer.writerow(task)
