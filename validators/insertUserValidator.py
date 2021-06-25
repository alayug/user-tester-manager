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
    emailRegex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    message = ""
    if email == "":
        message = "Email address can't be empty!"
    elif(re.search(emailRegex, email) == None):
        message = "Invalid email, it must consist of one '@', ends with '.' along with a minimum of two characters, and may not consist of special characters."
    return message

#phone number
def phoneNumberValidator(phoneNumber):
    phoneNumberRegex = '[0-9]{3}-[0-9]{3}-[0-9]{4}'
    message = ""
    if phoneNumber == "":
        message = "Phone number can't be empty!"
    elif(re.search(phoneNumberRegex,phoneNumber) == None):
        message = "Invalid phone number, it must only contain numbers and - be in the following format: 111-222-3333"
    return message

#task id
# skipping as it will be changed to a dropdown selection
# validator will be in insertTaskValidator