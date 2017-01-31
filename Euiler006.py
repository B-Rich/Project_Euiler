
def addAll1():
    total = 0
    for i in range(1, 101):
        total += i*i
    return total


def addAll2():
    total = 0
    for i in range(1, 101):
        total += i
    return pow(total, 2)

result = addAll2() - addAll1()
print result
