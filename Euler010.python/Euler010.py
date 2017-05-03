
import functools as ft
import timeit

start = timeit.default_timer()

i = 200#범위 지정
arr = []
base = 2
tmp = base

rangeof = list(range(2, i+1))
try:
    while rangeof:
        while tmp <= i:
            if tmp in rangeof:
                rangeof.remove(tmp)
            tmp = base + tmp

        arr.append(base)
        print(rangeof[0])
        base = rangeof[0]
        tmp = base
except:
    pass


sum = ft.reduce(lambda x, y: x + y, [int(i) for i in arr])

print(sum)

stop = timeit.default_timer()
print("실행시간: " + str(stop - start))

