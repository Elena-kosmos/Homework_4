# задайте последовательность чисел. напишите программу
# которая выведет список неповторяющихся элементов исходной последовательности

import random
list = [random.randint(0,10) for i in range(5)]
print(list)
new_list = []
[new_list.append(i) for i in list if i not in new_list ]
print(new_list)