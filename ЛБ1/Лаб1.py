a = float(input("Введите a: "))
if a==0:
    while a==0:
        print('Ошибка будет деление на ноль: ')
        a = float(input("Введите a не равную 0: "))
b= float(input("Введите b:"))
if b==0:
    while b==0:
        print('Ошибка будет деление на ноль: ')
        b = float(input("Введите b не равную 0: "))
c= float(input("Введите c:"))
d= float(input("Введите d:"))
k= float(input("Введите k:"))
f=abs((a*a-pow(b,3)-pow(c,3)*a*a)*(b-c+c*(k-d/pow(b,3)))-pow((k/b-k/a)*c,2)-20000)
print("ответ:"+str(f))
input("Нажмите Enter чтобы выйти\n")