# вычислить число Пи с заданной точностью d
# при d = 0,001 пи=3,141
# при d = 0,0001 пи=3,1415

import math
pi = math.pi
print('Pi =', pi)
d = 0.0001
print(f'accuracy = {d}')
count = 0
while d <1:
    count +=1
    d=d*10
print(round(pi,count))

