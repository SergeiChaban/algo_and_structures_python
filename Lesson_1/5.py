#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.


a = input('Введите две буквы в английской раскладке. Введите первую ')
b = input('Введите вторую букву ')
a = a.lower()
b = b.lower()

abc = (ord(a))
abc = abc - 96
print(abc)
if abc > 26:
    print('Вы ввели букву не в англиской раскладке')
else:
    print('Первая буква:', a, 'в алфавите под номером: ', abc)

abc2 = ord(b)
abc2 = abc2 - 96
if abc > 26:
    print('Вы ввели букву не в англиской раскладке')
else:
    print('Первая буква:', b, 'в алфавите под номером: ', abc2)

difference = abs(abc - abc2)
print('Количество букв между ними: ', difference)
