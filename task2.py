def print_a_to_b(a, b):
    print(a, end=' ', flush=True)
    if a == b:
        return
    if a < b:
        print_a_to_b(a + 1, b)
    else:
        print_a_to_b(a - 1, b)

a = int(input("Введіть A: "))
b = int(input("Введіть B: "))
print_a_to_b(a, b)
print()