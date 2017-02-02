import math

'''result = []
base = 2
register = base

num = list(range(3,  10000000))

while num:
    while register < 10000000:
        if register in num:
            num.remove(register)
        register = register + base
        print(register)
    result.append(base)
    base = num[0]
    register = base
    del num[0]
    print(str(len(result)) + " = len")
    if len(result) == 10002:
        print (result)


result.append(base)
print(result[-1])'''


result = [2]
tmp = []
i = 1
while True:
    print(i)
    i = i + 2
    sqrtRange = range(1, i)
    for n in sqrtRange:
        print n
        if i % n != 0:
            tmp.append(True)
        elif i % n == 0:
            tmp.append(False)
    if False in tmp == False:
        result.append(i)
    if len(result) == 10001:
        print(result[-1])
        break






