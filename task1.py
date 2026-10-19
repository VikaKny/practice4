def print_1_to_n(n):
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=' ', flush=True)

n = int(input("Введіть n: "))
print_1_to_n(n)
print()