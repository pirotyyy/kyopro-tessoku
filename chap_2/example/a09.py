def main():
    H, W, N = map(int, input().split())
    A = [None] * N
    B = [None] * N
    C = [None] * N
    D = [None] * N
    Z = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
    S = [[0 for _ in range(W + 1)] for _ in range(H + 1)]

    for i in range(N):
        A[i], B[i], C[i], D[i] = map(int, input().split())

    for i in range(N):
        Z[C[i]][D[i]] += 1
        Z[A[i] - 1][B[i] - 1] += 1
        Z[A[i] - 1][D[i]] -= 1
        Z[C[i]][B[i] - 1] -= 1

    # horizontal
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            S[i][j] = S[i][j - 1] + Z[i - 1][j - 1]

    # vertical
    for j in range(1, W + 1):
        for i in range(1, H + 1):
            S[i][j] = S[i - 1][j] + S[i][j]

    # output
    for i in range(1, H + 1):
        print(" ".join(str(s) for s in S[i][1:]))


if __name__ == "__main__":
    main()
