import re
import pandas as pd
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


data = pd.read_csv("cars.csv")

data_array = data.values

header = "Make,Model,Year,Body Type,Engine,Horsepower,Torque,MSRP (USD),City MPG,Highway MPG,0-60 mph (sec)\n"

accepted_file = open("accepted_cars.csv", "w", newline="")
accepted_file.write(header)
accepted_writer = csv.writer(accepted_file)

not_accepted_file = open("not_accepted_cars.csv", "w", newline="")
not_accepted_file.write(header)
not_accepted_writer = csv.writer(not_accepted_file)

for row in data_array:
    make = row[0]
    model = row[1]
    year = row[2]
    body_type = row[3]
    engine = row[4]
    horse_power = row[5]
    torque = row[6]
    msrp = row[7]
    city_mpg = row[8]
    highway_mpg = row[9]
    zero_to_sixty = row[10]

    if (isDataEmpty(make) or isDataEmpty(model) or isDataEmpty(year) or isDataEmpty(body_type) or isDataEmpty(engine) or isDataEmpty(horse_power) or isDataEmpty(torque) or isDataEmpty(msrp) or isDataEmpty(city_mpg) or isDataEmpty(highway_mpg) or isDataEmpty(zero_to_sixty)):
        not_accepted_writer.writerow(row)

    horse_power = re.split(" ", horse_power)[0]
    torque = re.split(" ", torque)[0]

    new_row = [make, model, year, body_type, engine, horse_power, torque, msrp, city_mpg, highway_mpg, zero_to_sixty]
    accepted_writer.writerow(new_row)

    
