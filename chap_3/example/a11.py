def binary_search(A, x):
    """
    @param A: array
    @param x: target number
    @return index if target.exist else -1
    """

    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if x < A[m]:
            r = m - 1
        elif x == A[m]:
            return m
        else:
            l = m + 1

    return -1


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    print(binary_search(A, X) + 1)


if __name__ == "__main__":
    main()
