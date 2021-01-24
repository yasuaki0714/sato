import statistics
import math

a = []

for j in range(5):
  print(j+1, "番目")
  b = float(input("入力"))
  a.append(b)

print("平均値", statistics.mean(a))
print("標準偏差", statistics.stdev(a))