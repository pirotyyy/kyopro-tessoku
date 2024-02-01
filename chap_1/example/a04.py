# Binary Reppresentation


def main():
    N = int(input())
    ans = ""

    for i in range(10):
        ans = str((N // (2**i)) % 2) + ans

    print(ans)


if __name__ == "__main__":
    main()
