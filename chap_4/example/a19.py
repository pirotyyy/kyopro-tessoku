def main():
    N, W = map(int, input().split())
    w = [None] * (N + 1)
    v = [None] * (N + 1)

    for i in range(1, N + 1):
        w[i], v[i] = map(int, input().split())

    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    # i = 0
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(W + 1):
            if j < w[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

    print(max(dp[N]))


if __name__ == "__main__":
    main()
