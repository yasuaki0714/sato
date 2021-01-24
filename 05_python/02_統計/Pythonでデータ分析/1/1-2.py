import numpy as np

date = [10, 30, 20, 50]
print('date=', date)
v_sum = np.sum(date)
print('sum=', v_sum)
v_mean = np.mean(date)
print('mean=', v_mean)
v_var = np.var(date)
print('var=', v_var)
v_std = np.std(date)
print('v_std=', v_std, '  v_std**2=', v_std**2)