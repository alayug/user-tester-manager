import csv


# Takes in list with following values - first_name,last_name,email_address,phone_number,task_id
def insert_user(firstname, lastName, emailAddress, phoneNumber, taskID):

    fields=[firstname, lastName, emailAddress, phoneNumber, taskID]

    # Insert new row in users.csv with list
    with open(r'C:\bench\user-tester-manager\database\users.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
