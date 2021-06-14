import csv

# Takes in parameters with following values - first_name,last_name,email_address,phone_number,task_id
def insert_user(firstname, lastName, emailAddress, phoneNumber, taskID):

    # put parameters into a list to insert to users.csv
    fields=[firstname, lastName, emailAddress, phoneNumber, taskID]

    # Insert new row in users.csv with list, using 'a' to append the data
    with open(r'C:\bench\user-tester-manager\database\users.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
