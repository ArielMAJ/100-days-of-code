import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data['temp'])
#
# print(data['temp'].mean())
# print(data['temp'].max())

# print(data[data.temp == data.temp.max()])

def c_to_f(x):
    return x*9/5+32

monday_rows = data[data.day=='Monday']
monday_temperatures = monday_rows.temp

print(monday_temperatures.apply(c_to_f))

