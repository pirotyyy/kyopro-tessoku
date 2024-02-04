import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    A.sort()
    for _ in range(Q):
        x = int(input())
        print(bisect.bisect_left(A, x))


if __name__ == "__main__":
    main()
