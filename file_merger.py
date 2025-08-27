import pandas as pd
import time

not_accepted_data = pd.read_csv("not_accepted_data.csv")
accepted_data = pd.read_csv("accepted_data.csv")

merged_data = pd.concat([accepted_data, not_accepted_data])
merged_data.to_csv("fake_data.csv", index = False)

time.sleep(1)

import data_analyzer