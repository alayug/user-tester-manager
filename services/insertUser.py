import csv

# Takes in list with list of the following values - first_name,last_name,email_address,phone_number,task_id
def insert_user(newUserList, appendOrWrite):
    # Insert new row in users.csv with list, using 'a' to append the data
    with open(r'database\users.csv', appendOrWrite, newline='') as f:
        writer = csv.writer(f)
        # For each item in the newUserList, append to users.csv
        for user in newUserList:
            writer.writerow(user)
