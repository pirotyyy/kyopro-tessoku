def main():
    N = int(input())
    H = list(map(int, input().split()))

    dp = [None] * N
    dp[0] = 0
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        dp[i] = min(abs(H[i] - H[i - 1]) + dp[i - 1], abs(H[i] - H[i - 2]) + dp[i - 2])

    P = [N - 1]
    place = N - 1
    while True:
        if place == 0:
            break

        if dp[place - 1] + abs(H[place] - H[place - 1]) == dp[place]:
            place = place - 1
        else:
            place = place - 2

        P.append(place)

    print(len(P))
    print(" ".join(str(P[i] + 1) for i in range(len(P) - 1, -1, -1)))


if __name__ == "__main__":
    main()
