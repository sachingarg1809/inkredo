import helperFunction
import numpy as np

data = helperFunction.readFile()

sorted_data, day = helperFunction.sortDataByTime(data)

gr_a_click_count = 0
gr_b_click_count = 0

day_count = 0
curr_day = 0
for i, log in enumerate(sorted_data):
    if day[i]>curr_day:
        curr_day = day[i]
        day_count += 1
    #whenever user visits a page, action = 'visitPage'
    if log[4]=='visitPage':
        if log[3]=='a':
            gr_a_click_count += 1
        elif log[3]=='b':
            gr_b_click_count += 1

search_a, search_b = helperFunction.totalSearches(data)
total_daily_click = (gr_a_click_count+gr_b_click_count)
gr_a_avg_click = gr_a_click_count/day_count
gr_b_avg_click = gr_b_click_count/day_count

print("Numbner of days: " + str(day_count))
print("Total click: " +str(total_daily_click))
##print(gr_a_click_count)
##print(gr_b_click_count)
print("Average click per day by Group A: " + str(gr_a_avg_click))
print("Average click per day by Group A: " + str(gr_b_avg_click))
