# Exausive Search


def main():
    A, B = map(int, input().split())
    ans = False

    for i in range(A, B + 1):
        if 100 % i == 0:
            ans = True

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
