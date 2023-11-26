f = open('content.txt', 'r')
content = f.read()
print(content)
f.close()

f = open('content.txt', 'r')
for line in f:
    print(line)
f.close()

f = open('text.txt', 'w')
f.write('1 \n')
f.close()

f = open('text.txt', 'a')
#mas = [i for i in range(20)]
mas = [2, 3]
for text in mas:
    f.write(str(text) + '\n')
f.close()