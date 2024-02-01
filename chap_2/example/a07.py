# Event Attendance


def main():
    D = int(input())
    N = int(input())
    B = [0] * (D + 1)
    Answer = [0] * (D + 1)

    for i in range(N):
        L, R = map(int, input().split())
        B[L - 1] += 1
        B[R] -= 1

    for i in range(1, D + 1):
        Answer[i] = Answer[i - 1] + B[i - 1]

    for i in range(1, D + 1):
        print(Answer[i])


if __name__ == "__main__":
    main()
