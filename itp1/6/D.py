def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [int(input()) for _ in range(m)]
    for i in range(n):
        ans = 0
        for j in range(m):
            ans += a[i][j] * b[j]
        print(ans)


main()
