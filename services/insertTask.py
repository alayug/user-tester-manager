import csv

# Takes in a list of task, and writeOrAppend ('w' or 'a')
def insert_task(newTaskList, writeOrAppend):
    # open file tasks.csv and insert new row in with task id and name, using 'a' to append the data
    with open(r'database\tasks.csv', writeOrAppend, newline='') as f:
        writer = csv.writer(f)
        # for each task in the list, append to csv
        for task in newTaskList:
            writer.writerow(task)
