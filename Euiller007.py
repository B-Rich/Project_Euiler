result = []
base = 2
register = base

num = list(range(3,  2147483647))

while num:
    while register <  2147483647:
        if register in num:
            num.remove(register)
        register = register + base
    result.append(base)
    base = num[0]
    register = base
    del num[0]


result.append(base)
print(result[10000])

