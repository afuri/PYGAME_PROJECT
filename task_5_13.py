ls = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 3 == 0:
        bin_n += bin_n[:2]
    else:
        bin_n = bin((bin_n.count('1') % 3) * 3)[2:] + bin_n
    r = int(bin_n, 2)
    if r <= 60:
        ls.append(n)
print(max(ls))

