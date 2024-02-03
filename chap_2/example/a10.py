def main():
    N = int(input())
    A = list(map(int, input().split()))
    D = int(input())
    L = [None] * D
    R = [None] * D

    for i in range(D):
        L[i], R[i] = map(int, input().split())

    P = [0] * N
    P[0] = A[0]
    for i in range(1, N):
        P[i] = max(P[i - 1], A[i])

    Q = [0] * N
    Q[N - 1] = A[-1]
    for i in range(N - 2, -1, -1):
        Q[i] = max(Q[i + 1], A[i])

    for i in range(D):
        print(max(P[L[i] - 2], Q[R[i]]))


if __name__ == "__main__":
    main()
