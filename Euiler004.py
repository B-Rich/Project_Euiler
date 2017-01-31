def is_Palindrome(n):

    n = str(n)
    reverse_n = n[::-1]

    if reverse_n == n:
        return True

hundreds = list(range(100, 1000))
tmp = []



for i in hundreds:
    for j in hundreds:
        number = i * j
        if is_Palindrome(number) == True:
            tmp.append(number)


tmp.sort()
print(tmp.pop())