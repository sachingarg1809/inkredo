import helperFunction
import numpy as np

data = helperFunction.readFile()

sorted_data, day = helperFunction.sortDataByTime(data)

gr_a_zero_count = 0
gr_b_zero_count = 0
curr_day = 0
day_count = 0

for i, log in enumerate(sorted_data):
    #number of search results are shown only for searchResultPage
    if day[i]>curr_day:
        curr_day = day[i]
        day_count += 1
    if log[4]=='searchResultPage' and (log[7]=='NA' or log[7]=='0'):
        if log[3]=='a':
            gr_a_zero_count += 1
        elif log[3]=='b':
            gr_b_zero_count += 1

search_a, search_b = helperFunction.totalSearches(data)
total_daily_zero_count = (gr_a_zero_count+gr_b_zero_count)
gr_a_avg_zero = gr_a_zero_count/day_count
gr_b_avg_zero = gr_b_zero_count/day_count

print("Numbner of days: " + str(day_count))
print("Total zero result searches: " +str(total_daily_zero_count))
print("Average zero result searches per day by Group A: " + str(gr_a_avg_zero))
print("Average zero result searches per day by Group A: " + str(gr_b_avg_zero))
