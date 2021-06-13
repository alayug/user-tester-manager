import csv

# Takes in task name
def get_user_details():
    # Create list to store the csv data
    userDetailsList = []

    # opens csv file
    with open(r'C:\bench\user-tester-manager\database\users.csv', 'r') as f:
        # csv reader will each line of data in the csv file
        reader = csv.reader(f)
        # for each row in the csv file, append to userDetailsList
        for row in reader:
            userDetailsList.append(row)
  
    return userDetailsList
