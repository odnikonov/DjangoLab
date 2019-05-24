import random
my_number = random.randint(1,10)
user_number = int(input('user_number: '))
while my_number != user_number:
    user_number = int(input('user_number: '))
print('Рандомно загаданное число число: ' + str(my_number))
input('Нажмите Enter для выхода из программы\n')