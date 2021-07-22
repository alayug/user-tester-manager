def taskNameValidator(taskName):
    message = ""
    if taskName == "" or taskName.isspace() == True:
        message = "Task Name can't be empty!"
    elif len(taskName) > 50:
        message = "Task Name can't be more than 50 characters"
    return message