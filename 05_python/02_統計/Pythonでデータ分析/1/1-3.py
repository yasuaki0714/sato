import numpy as np

date = [10, 30, 20, 50]
print('date=', date)
v_min = np.amin(date)
print('v_min = ', v_min)
v_med = np.median(date)
print('v_median = ', v_med)
v_max = np.amax(date)

Q1 = np.percentile(date, 25)
Q2 = np.percentile(date, 50)
Q3 = np.percentile(date, 75)
print('Q1 = {0}  Q2 = {1}  Q3 = {2}'.format(Q1, Q2, Q3))