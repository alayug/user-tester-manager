# Takes in task name

# Insert new row in tasks.csv with task name
import csv



def insertTask(taskID, taskName):

    fields=[taskID,taskName]

    with open(r'C:\bench\user-tester-manager\database\tasks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


insertTask(1,"test")