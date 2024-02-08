def main():
    N = int(input())
    H = list(map(int, input().split()))

    dp = [None] * N
    dp[0] = 0
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        dp[i] = min(abs(H[i] - H[i - 1]) + dp[i - 1], abs(H[i] - H[i - 2]) + dp[i - 2])

    print(dp[-1])


if __name__ == "__main__":
    main()
