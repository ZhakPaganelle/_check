from scipy.stats import kurtosis, skew

suka = []

for i in range(3):
    suka.append(0.075)

for i in range(35):
    suka.append(0.125)

for i in range(20):
    suka.append(0.175)

for i in range(10):
    suka.append(0.225)

for i in range(11):
    suka.append(0.275)

for i in range(4):
    suka.append(0.325)

for i in range(7):
    suka.append(0.375)

print('Kurtosis:', kurtosis(suka))
print('Skewness:', skew(suka))
