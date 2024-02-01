def main():
    T = int(input())
    N = int(input())
    L = [0] * N
    R = [0] * N
    B = [0] * (T + 1)
    Answer = [0] * (T + 1)

    for i in range(N):
        L[i], R[i] = map(int, input().split())

    for i in range(N):
        B[L[i]] += 1
        B[R[i]] -= 1

    for i in range(1, T + 1):
        Answer[i] = Answer[i - 1] + B[i - 1]

    for i in range(1, T + 1):
        print(Answer[i])


if __name__ == "__main__":
    main()
