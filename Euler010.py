import sys


base = 2
register = base
i = 2000000
result = []


num = list(range(3, i))
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

    if 4 in result:
        result.remove(4)

print(sum(result))


