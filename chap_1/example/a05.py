def main():
    N, K = map(int, input().split())
    ans = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if K - i - j >= 1 and K - i - j <= N:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
