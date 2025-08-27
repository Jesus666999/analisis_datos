from faker import Faker
import random
import re
import csv

fake = Faker()

header = ["first_name", "last_name", "email", "phone", "gender", "age"]
file = open("fake_data.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(header)

dirty_counter = 0

for _ in range(100):
    unlucky = random.randint(1, 10)
    last_name = fake.last_name()
    email = fake.free_email()
    phone = fake.basic_phone_number()
    gender = fake.passport_gender()
    age = random.randint(18, 75)

    if (str(gender) == "M"):
        first_name = fake.first_name_male()
    if (str(gender) == "F"):
        first_name = fake.first_name_female()
    else:
        first_name = fake.first_name()

    if (unlucky == 4):
        first_name += str(fake.random_digit())
        dirty_counter += 1
    
    if (unlucky == 9):
        last_name = ""
        dirty_counter += 1

    if (unlucky == 1):
        age = random.randint(-18, 17)
        dirty_counter += 1

    if (unlucky == 7):
        email = re.split("@", email)[0]
        dirty_counter += 1

    data_row = [first_name, last_name, email, phone, gender, age]
    writer.writerow(data_row)

print("Done...\nDirty data: ", dirty_counter)
