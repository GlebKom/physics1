import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
f = open('measurements.txt')
measurements = f.readlines()
for line in measurements:
    line = line.replace(',', '.')
measurements = [float(line.replace(',', '.').rstrip()) for line in measurements]

sr = sum(measurements)/len(measurements)
measurements_2 = [i - sr for i in measurements]
measurements_3 = [i**2 for i in measurements_2]
k = len(measurements_3)
# выборочное среднеквадратичное отклонение
sigma = (sum(measurements_3) / (k - 1))**0.5
abs_pogr = (2.01 * sigma) / (k**0.5)
otn_pogr = (abs_pogr / sr)*100

# макс. значение плотности распределения
pmax = 1 / (sigma*np.sqrt(2 * np.pi))

# ср.квадр. отклонение среднего значения
sigma_2 = (sum(measurements_3) / (k*(k - 1)))**0.5

# доверительный интервал
dt = 2.01*sigma_2
fig, ax = plt.subplots()
n, bins, patches = ax.hist(measurements, 10, edgecolor = 'black', density=True)

# 1-ый столбец табл.2  
print(bins)

cnt = [0 for i in range(10)]
for elem in measurements:
    for i in range(1, len(bins)):
        if bins[i-1] <= elem <= bins[i]:
            cnt[i-1] += 1
            break
        
# 2-ый столбец табл.2
print(cnt)

# 3-ый столбец табл.2        
cnt = [(cnt[i] / k)/(bins[i+1]-bins[i]) for i in range(len(cnt))]        
print(cnt)

# 4-ый столбец табл.2
bins2 = [(bins[i-1]+bins[i]) / 2 for i in range(1, len(bins))]
bins = np.asarray(bins2)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - sr))**2))

# значения плотностей вер-тей, пятый столбец
print(y)

ax.plot(bins, y, '-')
n1 = 0
n2 = 0
n3 = 0
for el in measurements:
    if sr-sigma <= el <= sr+sigma:
        n1 += 1
        n2 += 1
        n3 += 1
    elif sr-2*sigma <= el <= sr-sigma or sr+sigma <= el <= sr+2*sigma:
        n3 += 1
        n2 += 1
    elif sr-3*sigma <= el <= sr-2*sigma or sr+2*sigma <= el <= sr+3*sigma:
        n3 += 1
p1 = n1 / k
p2 = n2 / k
p3 = n3 / k
print(bins)
print(pmax)
print(sigma_2)
print(dt)
print(k)
print("Первый интервал"+str(sr-sigma)+'-'+str(sr+sigma))
print("Второй интервал"+str(sr-2*sigma)+'-'+str(sr+2*sigma))
print("Третий интервал"+str(sr-3*sigma)+'-'+str(sr+3*sigma))
print(n1)
print(n2)
print(n3)
print("Вероятности:")
print(p1)
print(p2)
print(p3)
plt.show()
