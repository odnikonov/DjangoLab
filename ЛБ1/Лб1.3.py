import random
l = []
k=0
for i in range(0,random.randint(5,20)):
    l.append(random.randint(-15,15))

for i in l:
    if 1<=i<=10:
        k+=i
print('Числа в масиве: ' + str(l))
print('Сложение всех чисел от 1 до 10 = ' + str(k))
input("Нажмите Enter для выхода из програмы\n")