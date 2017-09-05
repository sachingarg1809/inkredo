import csv
import numpy as np

def readFile(filename = 'events_log.csv'):
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for line in reader:
            data.append(line)

    data = np.array(data)
    print('Events log stored in numpy array')
    return data


#case 2.0xxxe+y not handeled
def sortDataByTime(data):
    day = data[:,1]
    for i in range(data.shape[0]):
        day[i] = day[i][6:8]

    day = day.astype(int)
    time_sorted_indices = np.argsort(day)

    ##print(time_sorted_indices.shape)
    '''
    sorted_data = data
    for i in range(data.shape[0]):
        sorted_data[i] = data[time_sorted_indices[i],:]
    '''
    sorted_data = data[time_sorted_indices,:]
    day = day[time_sorted_indices]
    return sorted_data, day

def totalSearches(data):
    gr_a_search_count = 0
    gr_b_search_count = 0
    for log in data:
        if log[4]=='searchResultPage':
            if log[3]=='a':
                gr_a_search_count += 1
            elif log[3]=='b':
                gr_b_search_count += 1
    return gr_a_search_count, gr_b_search_count
            
