# with open('./weather_data.csv') as f:
#     data = [line.split(',') for line in f.read().split('\n')]
# print(data)
#
# import csv
#
# with open('weather_data.csv') as f:
#     data = csv.reader(f)
#     temperature = []
#     for row in data:
#         try:
#             temperature.append(int(row[1]))
#         except:
#             continue
# print(temperature)
