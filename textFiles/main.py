"""
f = open('content.txt', 'r') #r a w r+
content = f.read() #readline() readlines()
print(content)
f.close()

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
"""
#seek(a, b), 0 : устанавливает начальную точку в начало файла (используется по умолчанию) • 1 : устанавливает начальную точку в текущую позицию • 2 : устанавливает начальную точку в конец файла
#tell()

mas = [2, 3]
with open('text.txt', 'r+') as f:
    for text in mas:
        f.write(str(text))