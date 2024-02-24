def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [None] * (N + 1)
    dp[1] = 0
    dp[2] = A[0]
    for i in range(3, N + 1):
        dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])

    p = N
    Ans = [N]
    while p >= 2:
        if dp[p] == dp[p - 1] + A[p - 2]:
            p = p - 1
        else:
            p = p - 2

        Ans.append(p)

    print(len(Ans))
    print(" ".join(str(Ans[i]) for i in range(len(Ans) - 1, -1, -1)))


if __name__ == "__main__":
    main()
