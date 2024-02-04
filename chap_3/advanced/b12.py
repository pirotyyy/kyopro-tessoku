def main():
    N = int(input())
    f = lambda x: x**3 + x

    l = 0.0
    r = 100.0
    for _ in range(20):
        m = (l + r) / 2
        val = f(m)

        if val > N:
            r = m
        else:
            l = m

    print(m)


if __name__ == "__main__":
    main()
