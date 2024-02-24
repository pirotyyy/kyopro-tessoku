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

    p = N
    Ans = [N]
    while p >= 2:
        if dp[p] == dp[p - 1] + abs(h[p - 1] - h[p - 2]):
            p = p - 1
        else:
            p = p - 2

        Ans.append(p)

    print(len(Ans))
    print(" ".join(str(Ans[i]) for i in range(len(Ans) - 1, -1, -1)))


if __name__ == "__main__":
    main()
