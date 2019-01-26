def main():
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        print('#' * W)
        for _ in range(H - 2):
            col = '#'
            for _ in range(W - 2):
                col += '.'
            col += '#'
            print(col)
        print('#' * W)
        print()


main()
