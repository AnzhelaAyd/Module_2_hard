def chislo(a):
    k = ''
    for i in range(1, a):
        for j in range(i + 1, a):
            if j <= i:
                continue
            if a % (i + j) == 0:
                k = k + str(i) + str(j)
    return k




for a in range(3, 21):
    b=chislo(a)
    print(b)
