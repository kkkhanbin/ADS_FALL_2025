n = int(input())
deg = int(input())

def bin_pow(n, deg):
    if deg == 0:
        return 1;
    if deg % 2 == 0:
        half = bin_pow(n, deg / 2)
        return half * half
    return n * bin_pow(n, deg - 1)

print(bin_pow(n, deg))
