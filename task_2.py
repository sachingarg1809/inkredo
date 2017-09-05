import helperFunction
import numpy as np

data = helperFunction.readFile()

sorted_data, day = helperFunction.sortDataByTime(data)

result_pos_dict = {}
pos = []

for i, log in enumerate(sorted_data):
    #whenever user visits a page, action = 'visitPage'
    if log[4]=='visitPage' and log[8]!='NA':
        if not log[8] in pos:
            pos.append(log[8])
        if day[i] in result_pos_dict:
            result_pos_dict[day[i]].append(log[8])
        else:
            result_pos_dict[day[i]] = []
            result_pos_dict[day[i]].append(log[8])

day_wise_best_pos = {}

for date in result_pos_dict.keys():
    best_count = 0
    best_position = None
    for n_pos in pos:
        if result_pos_dict[date].count(n_pos)>best_count:
            best_count = result_pos_dict[date].count(n_pos)
            best_position = n_pos
    day_wise_best_pos[date] = (best_position, best_count)

print(day_wise_best_pos)
