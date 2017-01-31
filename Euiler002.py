after1 = []
result1 = []


a = 0
b = 1
while a <= 4000000:
    result1.append(a)
    tmp_b = b
    b = tmp_b + a
    a = tmp_b

for i in result1:
    if i % 2 == 0:
        after1.append(i)

print(sum(after1))