def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        if i * i >= num:
            break
    return True


print(is_prime(7))
print(is_prime(81))
