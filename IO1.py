with open('test1.txt','w') as f:
    a='100'
    f.write('今天天气不错')
    f.write(a)

with open('test1.txt','r') as f:
    s =f.read()
    print('open for read...')
    print(s)

with open('test1.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)