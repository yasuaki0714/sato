import matplotlib.pyplot as plt
import numpy as np

City = ['asahikawa', 'sapporo', 'hakodate', 'aomori', 'morioka','sendai', 'akita', 'yamagata', 'fukusima', 'tokyo','yokohama', 'kumagaya', 'tiba', 'mito', 'utunomiya','maehasi', 'koufu', 'nagano', 'niigata', 'toyama','kanazawa', 'fukui', 'nagoya', 'gifu', 'sizuoka','tu', 'osaka', 'kobe', 'kyoto', 'hikone','nara', 'wakayama', 'totori', 'matue', 'okayama','koti', 'fukuoka', 'saga', 'nagasaki', 'kumamoto','oita', 'miyazaki', 'kagosima', 'naha']

Htemp = [30.1, 30.7, 25.2, 26.0, 30.5, 25.3, 28.1, 31.4, 30.5, 29.1,28.5, 30.7, 28.3, 26.3, 29.5, 31.2, 32.0, 30.1, 26.4, 29.0,28.2, 29.4, 29.6, 29.6, 27.7, 26.9, 30.2, 28.3, 31.3, 28.0,31.1, 27.0, 30.0, 29.2, 29.8, 28.1, 29.5, 28.4, 28.5, 28.6,27.6, 29.3, 30.5, 28.4, 30.3, 28.3, 26.4, 28.7, 29.7]

Ltemp = [11.9, 14.5, 12.4, 12.8, 17.0, 18.1, 15.9, 16.0, 17.4, 18.5,19.4, 17.7, 19.1, 15.6, 17.5, 17.9, 16.2, 15.5, 17.2, 16.5,19.4, 18.7, 19.8, 19.6, 16.9, 19.4, 19.9, 18.9, 18.9, 17.4,17.1, 18.8, 15.9, 16.8, 16.6, 18.0, 16.7, 17.6, 17.9, 17.3,17.5, 20.5, 19.9, 18.7, 18.9, 18.4, 20.0, 21.9, 23.9]

plt.figure(figsize = (10,8)) # in inches
plt.xlim(24,34)
plt.ylim(10,25)
plt.title('Scatterplot of (Max.temp,Min.temp)\n',fontsize = 20)
plt.xlabel('Maximum Temperature ($^\circ\mathrm {C} $)')
plt.ylabel('Minimum Temperature ($^\circ\mathrm {C} $)')
plt.plot(Htemp, Ltemp, 'bo', alpha = 0.6)
for ID, H, L in zip(City, Htemp, Ltemp):
  plt.text(H + 0.1,L + 0.1, ID, color = 'b', alpha = 0.6)
MeanH = np.mean(Htemp)
plt.vlines(MeanH, 10, 25, linestyle = '--', color = '#00AAFFAA', label = 'Mean max.temp.({0:.1f}'.format(MeanH) + '$^\circ\mathrm{C}$)')
MeanL = np.mean(Ltemp)
plt.hlines(MeanL, 24, 34, linestyle = '--', color = '#00AAFFAA', label = 'Mean min.temp.({0:.1f}'.format(MeanL) + '$^\circ\mathrm{C}$)')
plt.legend()
plt.show()