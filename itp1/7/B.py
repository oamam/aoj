def main():
    ans = []
    while True:
        n, x = map(int, input().split())
        if (n, x) == (0, 0):
            break
        c = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if i + j + k == x:
                        c += 1
        ans.append(c)
    for a in ans:
        print(a)


main()
