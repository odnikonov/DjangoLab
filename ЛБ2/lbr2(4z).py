print('Пусть дана строка:\n')
l = 'Stydent 2 kyrsa Gruppa BST1703 Fakultet OTF2'
print(l)
new_str1 = ''
for i in l:
    if i.isalpha():
        new_str1 += i   
print('\nСтрока из букв:\n ' + new_str1)
input("\nНажмите Enter для выхода из програмы\n")