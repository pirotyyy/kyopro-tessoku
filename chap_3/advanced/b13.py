def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]

    # S[R[i] + 1] - S[i] <= K
    # R[i]は超えないindexの最大値
    R = [0] * (N + 1)
    for i in range(N + 1):
        if i == 0:
            R[i] = 0
        else:
            R[i] = R[i - 1]

        while R[i] < N and S[R[i] + 1] - S[i] <= K:
            R[i] += 1

    Ans = 0
    for i in range(len(R)):
        Ans += R[i] - i

    print(Ans)


if __name__ == "__main__":
    main()
