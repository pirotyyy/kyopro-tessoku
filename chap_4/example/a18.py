def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[None for _ in range(S + 1)] for _ in range(N + 1)]
    dp[0][0] = True

    # dp: i = 0
    for i in range(1, S + 1):
        dp[0][i] = False

    # dp: i >= 1
    for i in range(1, N + 1):
        for j in range(S + 1):
            if j < A[i - 1]:
                if dp[i - 1][j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                if dp[i - 1][j] | dp[i - 1][j - A[i - 1]]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

    if dp[N][S]:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
