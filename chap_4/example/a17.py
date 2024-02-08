def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [None] * N
    dp[0] = 0
    dp[1] = A[0]
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

    P = [N - 1]
    place = N - 1
    while True:
        if place == 0:
            break

        if dp[place - 1] + A[place - 1] == dp[place]:
            place = place - 1
        else:
            place = place - 2

        P.append(place)

    print(len(P))
    print(" ".join(str(P[i] + 1) for i in range(len(P) - 1, -1, -1)))


if __name__ == "__main__":
    main()
