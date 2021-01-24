import matplotlib.pyplot as plt

values = [24, 10 ,5]
index = [0, 1, 2]
plt.bar(index, values)
names = ['Psy>Clin', 'Psy=Clin', 'Others']
plt.xticks(index, names)
plt.show()