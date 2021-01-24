x = 2
rnew = 2
for i in range(10):
    r1 = rnew
    r2 = x / r1
    rnew = (r1 + r2) / 2
    print(r1, rnew, r2)