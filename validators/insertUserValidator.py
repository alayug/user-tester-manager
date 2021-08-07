import re

def firstNameValidator(firstName):
    message = ""
    if firstName == "":
        message = "First name can't be empty!"
    # if firstName are not only letters, return a message
    elif firstName.isalpha() != True:
        message = "First name must only contain letters!"
    return message
    
def lastNameValidator(lastName):
    message = ""
    if lastName == "":
        message = "Last name can't be empty!"
    # if lastName has non letters, return a message
    elif lastName.isalpha() != True:
        message = "Last name must only contain letters!"
    return message

def emailValidator(email):
    # regex for email address
    emailRegex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    message = ""
    if email == "":
        message = "Email address can't be empty!"
    # if email does not match the regex above, return a message with hints
    elif(re.search(emailRegex, email) == None):
        message = "Invalid email, it must consist of one '@', ends with '.' along with a minimum of two characters, and may not consist of special characters."
    return message

#phone number
def phoneNumberValidator(phoneNumber):
    phoneNumberRegex = '[0-9]{3}-[0-9]{3}-[0-9]{4}'
    message = ""
    if phoneNumber == "":
        message = "Phone number can't be empty!"
    # if phoneNumber does not match the regex, return message with hint
    elif(re.search(phoneNumberRegex,phoneNumber) == None):
        message = "Invalid phone number, it must only contain numbers and - be in the following format: 111-222-3333"
    return message
