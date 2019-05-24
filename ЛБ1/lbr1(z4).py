import random
l = []
string =""
for i in range(0,random.randint(5,20)):
    l.append(random.randint(-100,100))  
print('Числа в масиве: ' + str(l))
print('Минимальное число = ' + str(min(l)))
input("Нажмите Enter для выхода из програмы\n")
