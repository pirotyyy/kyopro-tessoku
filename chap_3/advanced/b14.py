import bisect


def Enumerate(A):
    SumList = []
    for i in range(2 ** len(A)):
        sum = 0
        for j in range(len(A)):
            if (i >> j) & 1:
                sum += A[j]

        SumList.append(sum)
    return SumList


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    L1 = A[: (N // 2)]
    L2 = A[(N // 2) :]

    Sum1 = Enumerate(L1)
    Sum2 = Enumerate(L2)
    Sum1.sort()
    Sum2.sort()

    for i in range(len(Sum1)):
        pos1 = bisect.bisect_left(Sum2, K - Sum1[i])
        if pos1 < len(Sum2) and Sum2[pos1] == K - Sum1[i]:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
