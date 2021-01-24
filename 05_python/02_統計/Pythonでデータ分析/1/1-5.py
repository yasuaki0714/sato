def replace0(d,c):
  d[0] = c

def replace(d,c):
  d = c

date = [10, 30, 20, 50]
print('date = ', date)

replace0(date, "a")
print('date = ', date)

v = 1
print('v = ', v)
replace(v,2)
print('v = ',v)