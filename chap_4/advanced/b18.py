def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[None for _ in range(S + 1)] for _ in range(N + 1)]

    # dp: i = 0
    dp[0][0] = True
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
                if dp[i - 1][j] or dp[i - 1][j - A[i - 1]]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

    if not dp[N][S]:
        print(-1)
        return

    Answer = []
    Place = S
    for i in reversed(range(1, N + 1)):
        if dp[i - 1][Place]:
            Place = Place - 0

        else:
            Place = Place - A[i - 1]
            Answer.append(i)

    Answer.reverse()

    print(len(Answer))
    print(" ".join(str(i) for i in Answer))


if __name__ == "__main__":
    main()
