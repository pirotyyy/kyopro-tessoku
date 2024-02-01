# ビット全探索で部分和問題を解く


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = False

    for i in range(2**N):
        sum = 0

        for j in range(N):
            if (i >> j) & 1:
                sum += A[j]

        if sum == K:
            ans = True

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
