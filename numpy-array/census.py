# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
#Code starts here
census = np.concatenate((data, new_record), axis = 0)
print(census.shape)
age = np.array(census[: , 0])
max_age = np.max(age)
min_age = np.min(age)
age_mean = age.mean()
age_std = np.std(age)
print(max_age , min_age , age_mean , age_std)


_0 = census[: , 2] == 0
_1 = census[: , 2] == 1
_2 = census[: , 2] == 2
_3 = census[: , 2] == 3
_4 = census[: , 2] == 4

race_0 = census[_0]
race_1 = census[_1]
race_2 = census[_2]
race_3 = census[_3]
race_4 = census[_4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
f = 0
_race = np.array([len_0, len_1, len_2, len_3, len_4])
_min = np.min(_race)
for i in _race:
    if _min == i:
        minority_race = f
    else:
        f += 1
print(minority_race)

_citizens = census[: , 0] > 60
senior_citizens = census[_citizens]
working_hours_sum = senior_citizens[: , 6].sum()
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print('%.2f' % avg_working_hours)

_high = census[: , 1] > 10
high = census[_high]

_low = census[: , 1] <= 10
low = census[_low]

avg_pay_high = high[: , 7].mean()
avg_pay_low = low[: , 7].mean()
print('%.2f' % avg_pay_high , '%.2f' % avg_pay_low)
