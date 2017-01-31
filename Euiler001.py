after = []
result = 0





for i in list(range(1000)):
    if i % 3  == 0 or i % 5 == 0:
        after.append(i)
    else:
        pass

for i in after:

    result = i + result

print(result)