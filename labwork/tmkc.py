def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def sumPrime(n, i=2):
    if i > n:
        return False

    if is_prime(i) and is_prime(n - i):
        print(f"{n} = {i} + {n - i}")
        return True
    # Recurse with next number
    return sumPrime(n, i + 1)

if __name__ == '__main__':

num = int(input("Enter a number: "))
if sumPrime(num):
    print("YES, it can be expressed as the sum of two prime numbers.")
else:
    print("NO, it cannot be expressed as the sum of two prime numbers.")