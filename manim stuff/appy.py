def is_good_number(n: int) -> bool:
    digits=str(n)
    return len(digits) == 10 and set(digits) == set("0123456789")

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False
    else:
        return True
LOWER_LIMIT = 1023456789
UPPER_LIMIT = 9876543210
solutions = 0
for q in range(2, 2144):  # because 2143 is the largest prime with its cube less than the maximum 
    if not is_prime(q):
        continue
    q_cubed = q ** 3
    min_p_squared = max(0, LOWER_LIMIT - q_cubed)
    p_start = int(min_p_squared ** 0.5)
    p_end = int((UPPER_LIMIT - q_cubed) ** 0.5)
    for p in range(p_start, p_end + 1):
        if is_prime(p):
            candidate = q_cubed + p * p
            if is_good_number(candidate):
                solutions += 1
print(solutions)