import pandas as pd
import re
import csv

def isAlphabetic(data):
    if (not re.search("[a-zA-z]+$", data)):
        print("Data " , data, " not accepted")
        return False
    else:
        return True

def isDataEmpty(data):
    if (re.search("^nan", str(data))):
        print("Row contains empty data: '",data,"'")
        return True
    else:
        return False

def isMailValid(mail):
    if (re.search("^[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]com", mail)):
        return True
    else:
        print("Email " , mail, " not accepted")
        return False

def isPhoneValid(phone_num):
    if (re.search("[0-9]{10}", phone_num)):
        return True
    else:
        print("Phone " , phone_num, " not accepted")
        return False

def normalizePhone(phone_num):
    phone_num = re.sub("[()-]", "", str(phone_num))
    return phone_num

def isGenderValid(gender):
    if (re.search("M|F", str(gender))):
        return True
    else:
        print("Gender " , gender, " not accepted")
        return False

def isAgeValid(age):
    if (re.search("18|19|[2-7][0-9]", str(age))):
        return True
    else:
        print("Age " , age, " not accepted")
        return False

data = pd.read_csv("fake_data.csv")
row_number, column_number = data.shape
array = data.values

header = data = "first_name,last_name,email,phone_number,gender,age\n"

accepted_file = open("accepted_data.csv", "w", newline="")
accepted_file.write(header)
accepted_writer = csv.writer(accepted_file)

not_accepted_file = open("not_accepted_data.csv", "w", newline="")
not_accepted_file.write(header)
not_accepted_writer = csv.writer(not_accepted_file)

for row in array:
    first_name = row[0]
    last_name = row[1]
    email = row[2]
    phone = row[3]
    gender = row[4]
    age = row[5]

    # Check for empty cells
    if (isDataEmpty(first_name) or isDataEmpty(last_name) or isDataEmpty(email) or isDataEmpty(phone) or isDataEmpty(gender) or isDataEmpty(age)):
        not_accepted_writer.writerow(row)
        continue
    
    # Check if first and last names contains ONLY alphabeticals 
    if (not isAlphabetic(first_name) or not isAlphabetic(last_name)):
        not_accepted_writer.writerow(row)
        continue
    
    # Check if email has correct structure
    if (not isMailValid(email)):
        not_accepted_writer.writerow(row)
        continue
    
    # Check if phone is valid and normalizes it 
    if (not isPhoneValid(normalizePhone(phone))):
        not_accepted_writer.writerow(row)
        continue
    else:
        phone = normalizePhone(phone)
    
    # Check if gender is valid
    if (not isGenderValid(gender)):
        not_accepted_writer.writerow(row)
        continue
    
    # Check if age is valid
    if (not isAgeValid(age)):
        not_accepted_writer.writerow(row)
        continue

    data_row = [first_name, last_name, email, phone, gender, age]
    accepted_writer.writerow(data_row)