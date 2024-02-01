def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = A[i - 1] + S[i - 1]

    for i in range(Q):
        L, R = map(int, input().split())
        result = S[R] - S[L - 1]

        if result < (R - L + 1) / 2:
            print("lose")
        elif result == (R - L + 1) / 2:
            print("draw")
        else:
            print("win")


if __name__ == "__main__":
    main()
