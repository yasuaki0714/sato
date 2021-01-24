# 定義
a = []
sum = 0
dev_sum = 0

n = int(input("データの個数を入力"))

#　入力
for j in range(n):
  print(j+1, "番目")
  b = float(input("入力"))
  a.append(b)

#　合計と相加平均を計算
for i in range(n):
  x_value = int(a[i-1])
  sum = sum + x_value
  ave = sum /(i+1)

#　偏差と偏差の2乗の和を計算
for i in range(n):
  dev = a[i] - ave
  dev2 = dev**2
  dev_sum = dev_sum + dev2

#　標準偏差の計算
dev_ave = dev_sum / 5
standard_dev = dev_ave**(1/2)
variation_coefficient = standard_dev / ave

#　出力
print(a)
print("合計", sum)
print("平均値", ave)
print("偏差の2乗の和", dev_sum)
print("分散", dev_ave)
print("標準偏差", standard_dev)
print("変動係数", variation_coefficient)