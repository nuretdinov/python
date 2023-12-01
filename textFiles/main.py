import os
print(os.getcwd())
print(os.path.exists('text.txt'))
print(os.listdir(os.getcwd()))



"""data = [1, 2, 3]
with open('text.txt', 'a') as f:
    for text in data:
        f.write(str(text))"""

"""f = open('text.txt')
for line in f:
    print(line)"""

"""
f = open('content.txt', 'r')
for line in f:
    print(line)
f.close()

f = open('text.txt', 'w')
f.write('1 \n') #writelines()
f.close()

f = open('text.txt', 'r+')
mas = [2, 3]
for text in mas:
    f.write(str(text))
f.close()

#seek(a, b), 0 : устанавливает начальную точку в начало файла (используется по умолчанию) • 1 : устанавливает начальную точку в текущую позицию • 2 : устанавливает начальную точку в конец файла
#tell()

mas = [2, 3]
with open('text.txt', 'r+') as f:
    for text in mas:
        f.write(str(text))

"""