
for k in range(3, 21):
    str_ = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                str_ = f'{i}{j}'
                print(k, str_)

