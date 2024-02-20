N = 15

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j - 1) == i):
            print("*", end="")
        else:
            print(" ", end="")
    print("")


def a_space_classic(n):
    z = n - 1
    x = 1
    for _ in range(0, n):
        for _ in range(0, z):
            print(" ", end="")
        for _ in range(0, x):
            print("+", end="")
        for _ in range(0, z):
            print(" ", end="")
        x = x + 2
        z = z - 1
        print()


a_space_classic(6)
