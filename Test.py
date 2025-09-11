import math
num = 1000000000
factors = []
for i in range(1, round(num/2)):
    if num % i == 0:
        factors.append(i)
    if len(factors)<71:
        continue
    else:
        break

print(factors[69])

num = 1000000000000
factors = []
for i in range(1, round(num/2)):
    if num % i == 0:
        factors.append(i)
    if len(factors)<71:
        continue
    else:
        break

print(factors[69])

