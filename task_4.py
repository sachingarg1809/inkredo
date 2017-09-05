import helperFunction
import numpy as np
from matplotlib import pyplot as plt

data = helperFunction.readFile()

checkin_time_dict = {} #key = page_id, value = check_in time
res_pos_dict = {} #key = page id, value = response position in search results

for log in data:
    key = log[6]
    if log[4]=='visitPage' and log[8]!='NA':
        res_pos_dict[key] = int(log[8])
    if log[4]=='checkin':
        if key in checkin_time_dict:
            if int(log[5])>checkin_time_dict[key]:
                checkin_time_dict[key] = int(log[5])
        else:
            checkin_time_dict[key] = int(log[5])

#relation response position and checkin time
rel_pos_checkin = {} #key = page id, value = (response position, checkin time)
list_pos_checkin = []

for key in checkin_time_dict.keys():
    if key in res_pos_dict.keys():
        rel_pos_checkin[key] = (res_pos_dict[key],checkin_time_dict[key])
        list_pos_checkin.append([res_pos_dict[key],checkin_time_dict[key]])

list_pos_checkin = np.array(list_pos_checkin)

plt.plot(list_pos_checkin[:,0],list_pos_checkin[:,1], '.')
plt.show()
        
