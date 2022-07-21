import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

column_names = ['Primary Fur Color', 'Count']
fur_color_count = data[column_names[0]].value_counts()

row_values = []
for k,v in fur_color_count.items():
    row_values.append([k,v])
# print(fur_color_count)

pd.DataFrame(row_values,columns=column_names).to_csv("squirrel_data.csv")
