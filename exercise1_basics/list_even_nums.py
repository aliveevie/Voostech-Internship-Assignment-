start, end = 1, 100
Even = []
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")
    else:
        (Even.append(num))
print('The Even numbers: ', Even)

