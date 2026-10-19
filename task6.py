def print_digits_direct(n):
    if n < 10:
        print(n, end=' ', flush=True)
        return
    print_digits_direct(n // 10)
    print(n % 10, end=' ', flush=True)

n = int(input("Введіть N: "))
print_digits_direct(n)
print()