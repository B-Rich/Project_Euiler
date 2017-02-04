import math

result = []
base = 2
register = base

num = list(range(3,  100))

while num:
    while register < 100:
        if register in num:
            num.remove(register)
        register = register + base
        print(register)
    result.append(base)
    base = num[0]
    register = base
    del num[0]
    print(str(len(result)) + " = len")

    print (result)


result.append(base)
print(result[-1])

#NoNo......Failed....
'''result = [2]
tmp = []
i = 1


while True:
    print(result)
    i = i + 2
    Range = range(3, math.sqrt(i) -1)
    for n in Range:
        if i % n == 0:
            break
        result.append(i)
    if len(result) == 10001:
        print(result[-1])
        break'''






