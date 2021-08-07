def taskNameValidator(taskName):
    message = ""
    if taskName == "" or taskName.isspace() == True:
        message = "Task Name can't be empty!"
    # if taskName is more than 50 characters, return a message with hint
    elif len(taskName) > 50:
        message = "Task Name can't be more than 50 characters"
    return message