import sys


base = 2
register = base
i = 100
result = []

while True:
    num = list(range(3, i))
    i += 10000
    while num:
        while register < i:
            if register in num:
                if register in result:
                    pass
                num.remove(register)
            register = register + base

        result.append(base)
        base = num[0]
        register = base
        del num[0]

        result = list(set(result))
        if 4 in result:
            result.remove(4)
        result.sort()
        print(str(len(result)) + " = len")
        print(result)
        if len(result) == 10001:
            print(result[10001])
            sys.exit()



result.append(base)
print(result)

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






