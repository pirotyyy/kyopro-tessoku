# Linear Search


def main():
    N, X = map(int, input().split())
    ans = False

    A = list(map(int, input().split()))

    for i in range(N):
        if A[i] == X:
            ans = True

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
