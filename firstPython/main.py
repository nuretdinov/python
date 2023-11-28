num1 = input('Введите первое число: ')
num2 = input('Введите второе число:')
sum = int(num1) + int(num2)
print('Сумма= ' + str(sum))

# int, float, str
# + - * / ** > < >= <= == != and or not

friends_list = ['Max', 'Ann', 'Roman']  # список
print(friends_list[2])

name_list = {'Max', 'Ann', 'Muhtar'}  # набор - неупорядоченный
guests = {'Max': 'boy', 'Ann': 'girl', 'Roman': 'boy'}  # кортеж (словарь)

i = 0
while i <= 10:
    print(i)
    i = i + 1

stop_word = ''
while stop_word != 'stop':
    print('+')
    stop_word = input('Введите стоп-слово: ')

for i in range(0, 5):
    print(i)

for name in friends_list:
    if name == 'Max':
        print('boy')
    elif name == 'Ann':
        print('girl')
    else:
        print('dog')

for name in friends_list:
    match name:
        case "Max":
            print('boy')
        case "Ann":
            print('girl')
        case _:
            print('dog')


# break, continue
def my_func(a, b):
    # global vars
    sum = a + b
    return sum


result = my_func(2, 5)
print(result)


# перехват исключений try expect
def my_func(a, b):
    try:
        return a / b
    except (ZeroDivisionError):
        return 'деление на ноль'


print(my_func(2, 2))

try:
    with open('text.txt', 'r') as f:
        print(f.read())
except (FileNotFoundError):
    print('Файл не найден')
finally:
    print('Все действия выполнены');

# raise errorName - вызывает необходимую ошибку
