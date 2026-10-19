def print_digits_reversed(n):
    if n == 0:
        return
    print(n % 10, end=' ', flush=True)
    print_digits_reversed(n // 10)

n = int(input("Введіть N: "))
if n == 0:
    print(0)
else:
    print_digits_reversed(n)
    print()