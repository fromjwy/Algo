def Z(size, x, y):
    if size == 1:
        return 0

    size //= 2
    for i in range(2):
        for j in range(2):
            if x < size*(i+1) and y < size*(j+1):
                return (i*2+j)*size*size + Z(size, x-size*i, y-size*j)


N, r, c = map(int, input().split())

print(Z(2**N, r, c))
