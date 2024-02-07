import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))

    X = list(set(A))
    X.sort()

    B = [None] * N
    for i in range(N):
        B[i] = bisect.bisect_left(X, A[i])
        B[i] += 1

    print(" ".join(str(b) for b in B))


if __name__ == "__main__":
    main()
