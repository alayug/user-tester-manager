from services.insertUser import insert_user
from services.getUserDetails import get_user_details

def delete_user(email):
    # get all the current users in users.csv
    currentUserList = get_user_details()
    # list to store the new data that will write over the current users.csv file
    newUserList = []

    for user in currentUserList:
        # if the row (users[2] = email) in users.csv does not match the email parameter, add to newUserList
        if str(user[2]) != str(email):
            newUserList.append(user)
    
    # replace everything in current users.csv with newUserList by passing in 'w' as second parameter
        insert_user(newUserList,'w')