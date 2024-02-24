def main():
    N = int(input())
    h = list(map(int, input().split()))

    dp = [None] * (N + 1)
    dp[1] = 0
    dp[2] = abs(h[1] - h[0])

    for i in range(3, N + 1):
        dp[i] = min(
            dp[i - 1] + abs(h[i - 1] - h[i - 2]), dp[i - 2] + abs(h[i - 1] - h[i - 3])
        )

    print(dp[-1])


if __name__ == "__main__":
    main()
