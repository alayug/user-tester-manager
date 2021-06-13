
import csv

# Takes in task name
def insert_task(taskID, taskName):
    fields=[taskID,taskName]

    # Insert new row in tasks.csv with task name, using 'a' to append the data
    with open(r'C:\bench\user-tester-manager\database\tasks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
