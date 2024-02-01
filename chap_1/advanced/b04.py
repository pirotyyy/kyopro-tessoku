def main():
    N = input()
    ans = 0

    for i in range(len(N)):
        ans += int(N[i]) * (2 ** (len(N) - 1 - i))

    print(ans)


if __name__ == "__main__":
    main()
