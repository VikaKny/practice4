def is_power_of_two(n):
    if n == 1:
        return "YES"
    if n < 1 or n % 2 != 0:
        return "NO"
    return is_power_of_two(n // 2)

n = int(input("Введіть N: "))
print(is_power_of_two(n))