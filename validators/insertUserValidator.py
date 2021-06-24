def firstNameValidator(firstName):
    message = ""
    if firstName == "":
        message = "First name can't be empty!"
    elif firstName.isalpha() != True:
        message = "First name must only contain letters!"
    return message
    
def lastNameValidator(lastName):
    message = ""
    if lastName == "":
        message = "Last name can't be empty!"
    elif lastName.isalpha() != True:
        message = "Last name must only contain letters!"
    return message