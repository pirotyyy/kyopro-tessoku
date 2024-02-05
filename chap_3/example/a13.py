# TLE
def zentansaku(N, K, A):
    S = []
    for i in range(N):
        for j in range(i + 1, N):
            S.append(A[j] - A[i])

    Ans = 0
    for i in range(len(S)):
        if S[i] <= 10:
            Ans += 1

    print(Ans)


# OK
import bisect


def binary_search(N, K, A):
    R = []
    for i in range(N):
        index = bisect.bisect_left(A, A[i] + K + 1) - 1
        R.append(index)

    Ans = 0
    for i in range(len(R)):
        Ans += R[i] - i

    print(Ans)


# OK
def shakutori(N, K, A):
    R = [0] * N
    for i in range(N):
        if i == 0:
            R[i] = 0
        else:
            R[i] = R[i - 1]

        while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
            R[i] += 1

    Ans = 0
    for i in range(len(R)):
        Ans += R[i] - i

    print(Ans)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    shakutori(N, K, A)


if __name__ == "__main__":
    main()
