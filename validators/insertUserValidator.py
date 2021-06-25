import re

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

def emailValidator(email):
    # regex for email address
    regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    message = ""
    if email == "":
        message = "Email address can't be empty!"
    elif(re.search(regex, email) == None):
        print(re.search(regex, email))
        message = "Invalid email, it must consist of one '@', ends with '.' along with a minimum of two characters, and may not consist of special characters."
    return message

#phone number

#task id