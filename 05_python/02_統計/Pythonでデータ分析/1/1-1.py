date = [10, 30, 20, 50]
print('date=', date)
sum = 0
for v in date:
  sum += v
print('sum=', sum)
mean = sum / len(date)
print('mean=', mean)

ssum = 0.0
for v in date:
  ssum +=(v - mean) ** 2
var = ssum / len(date)
print('var=', var)