def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = [0] * Q

    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = A[i - 1] + S[i - 1]

    for i in range(Q):
        L, R = map(int, input().split())
        ans[i] = S[R] - S[L - 1]

    for i in range(Q):
        print(ans[i])


if __name__ == "__main__":
    main()
