from services.insertTask import insert_task
from services.getTaskDetails import get_task_details

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