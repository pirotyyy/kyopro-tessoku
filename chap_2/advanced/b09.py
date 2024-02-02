def main():
    N = int(input())
    A = [None] * N
    B = [None] * N
    C = [None] * N
    D = [None] * N

    for i in range(N):
        A[i], B[i], C[i], D[i] = map(int, input().split())

    X = [[0 for _ in range(1501)] for _ in range(1501)]
    for i in range(N):
        X[A[i]][B[i]] += 1
        X[A[i]][D[i]] -= 1
        X[C[i]][B[i]] -= 1
        X[C[i]][D[i]] += 1

    for i in range(0, 1501):
        for j in range(1, 1501):
            X[i][j] = X[i][j - 1] + X[i][j]

    for i in range(1, 1501):
        for j in range(0, 1501):
            X[i][j] = X[i - 1][j] + X[i][j]

    # output
    Answer = 0
    for i in range(1501):
        for j in range(1501):
            if X[i][j] >= 1:
                Answer += 1

    print(Answer)


if __name__ == "__main__":
    main()
