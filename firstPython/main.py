"""
num1 = input('Введите первое число: ')
num2 = input('Введите второе число:')
sum = int(num1) + int(num2)
print('Сумма= ' + str(sum))
"""
#int, float, str
# + - * / ** > < >= <= == != and or not

friendsList = ['Max', 'Ann', 'Roman'] #список
print(friendsList[2])

nameList = {'Max', 'Ann', 'Muhtar'} #набор - неупорядоченный
guests = {'Max':'boy', 'Ann':'girl', 'Roman':'boy'} #словари

i=0
while i <= 10:
    print(i)
    i = i + 1

stopWord=''
while stopWord != 'stop':
    print('+')
    stopWord=input('Введите стоп-слово: ')

for i in range(0, 5):
    print(i)

for name in friendsList:
    if name == 'Max' : print('boy')
    elif name == 'Ann': print('girl')
    else: print('dog')

for name in friendsList:
    match name:
        case "Max": print('boy')
        case "Ann": print('girl')
        case _: print('dog')

#break, continue