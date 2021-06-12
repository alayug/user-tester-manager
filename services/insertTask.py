# Takes in task name

# Insert new row in tasks.csv with task name
import csv



def insert_task(taskID, taskName):

    fields=[taskID,taskName]

    with open(r'C:\bench\user-tester-manager\database\tasks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
