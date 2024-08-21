password = int(input('Введите число: '))
str_ = []
for k in range(3, password + 1):
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                str_.append(str(i) + str(j))

print('Число: ', password)
print('Пароль: ', *str_, sep='')
