def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1

    else:
        half = n//2

        if x <= X < x+half and y <= Y < y+half:
            solve(half, x, y)
        elif x <= X < x+half and y+half <= Y < y+n:
            result += half**2
            solve(half, x, y+half)
        elif x+half <= X < x+n and y <= Y < y+half:
            result += half**2*2
            solve(half, x+half, y)
        elif x+half <= X < x+n and y+half <= Y < y+n:
            result += half**2*3
            solve(half, x+half, y+half)


N, X, Y = map(int, input().split())
result = 0
solve(2**N, 0, 0)
