def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def check(x):
        Sum = 0
        for i in range(N):
            Sum += (x + 1) // A[i]
        if Sum >= K:
            return True
        return False

    l = 0
    r = 10**9 - 1
    while l < r:
        m = (l + r) // 2
        ans = check(m)
        if ans:
            r = m
        else:
            l = m + 1

    print(l + 1)


if __name__ == "__main__":
    main()
