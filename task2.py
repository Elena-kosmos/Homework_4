# задайте натурльное число N напишите программу
# которая составит список простых множителей числа N
# 6 -> [1,2,3] 144 ->[2,3]


num = int(input('Enter the number: '))
i =2
list =[]
old = num
while i<=num:
    if num % i ==0:
        list.append(i)
        num //= i
        i =2
    else:
        i +=1
print(f'простые множители числа {old}  приведены в списке: {list}')
