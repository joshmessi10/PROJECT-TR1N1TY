#1. is_prime(n): Checks if a given number is prime.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
#2. gcd(a, b): Computes the greatest common divisor of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#3. lcm(a, b): Computes the least common multiple of two numbers.
def lcm(a, b):
    return a * b // gcd(a, b)
#4. is_palindrome(s): Checks if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
#5. smallest_palindrome(digits): Finds the smallest palindrome with a given number of digits.
def smallest_palindrome(digits):
    start = 10**(digits - 1)
    end = 10**digits - 1
    for i in range(start, end):
        s = str(i)
        if s == s[::-1]:
            return i
#6. largest_palindrome(digits): Finds the largest palindrome with a given number of digits.
def largest_palindrome(digits):
    start = 10**digits - 1
    end = 10**(digits - 1)
    for i in range(start, end, -1):
        s = str(i)
        if s == s[::-1]:
            return i
#7. is_armstrong(n): Checks if a given number is an Armstrong number.
def is_armstrong(n):
    s = str(n)
    k = len(s)
    return n == sum(int(d)**k for d in s)
#8. is_perfect(n): Checks if a given number is a perfect number.
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
#9. is_abundant(n): Checks if a given number is an abundant number.
def is_abundant(n):
    return n < sum(i for i in range(1, n) if n % i == 0)
#10. is_deficient(n): Checks if a given number is a deficient number.
def is_deficient(n):
    return n > sum(i for i in range(1, n) if n % i == 0)
#11. is_pandigital(n): Checks if a given number is pandigital.
def is_pandigital(n):
    s = str(n)
    return all(str(i) in s for i in range(1, len(s) + 1))
#12. is_harshad(n): Checks if a given number is a Harshad number.
def is_harshad(n):
    return n % sum(int(d) for d in str(n)) == 0
#13. is_ugly(n): Checks if a given number is an ugly number.
def is_ugly(n):
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1
#14. is_happy(n): Checks if a given number is a happy number.
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1
#15. is_harmonic(n): Checks if a given number is a harmonic number.
def is_harmonic(n):
    return n == sum(1/i for i in range(1, n + 1))
#16. is_triangular(n): Checks if a given number is a triangular number.
def is_triangular(n):
    return (8*n + 1)**0.5 % 1 == 0
#17. is_square(n): Checks if a given number is a square number.
def is_square(n):
    return n**0.5 % 1 == 0
#18. is_pentagonal(n): Checks if a given number is a pentagonal number.
def is_pentagonal(n):
    return (24*n + 1)**0.5 % 6 == 5
#19. is_hexagonal(n): Checks if a given number is a hexagonal number.
def is_hexagonal(n):
    return (8*n + 1)**0.5 % 4 == 3
#20. is_heptagonal(n): Checks if a given number is a heptagonal number.
def is_heptagonal(n):
    return (40*n + 9)**0.5 % 10 == 7
#21. is_octagonal(n): Checks if a given number is an octagonal number.
def is_octagonal(n):
    return (3*n + 1)**0.5 % 3 == 0
#22. is_fibonacci(n): Checks if a given number is a Fibonacci number.
def is_fibonacci(n):
    return is_square(5*n**2 + 4) or is_square(5*n**2 - 4)


#6. factorial(n): Computes the factorial of a non-negative integer.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
#7. binomial(n, k): Computes the binomial coefficient "n choose k".
def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
#8. fibonacci(n): Computes the nth Fibonacci number.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
#9. collatz(n): Generates the Collatz sequence starting from a given number.
def collatz(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3*n + 1
    yield 1
#10. prime_factors(n): Generates the prime factors of a given number.
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n
#11. divisors(n): Generates the divisors of a given number.
def divisors(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                yield n // i
#12. sum_of_digits(n): Calculates the sum of the digits of a number.
def sum_of_digits(n):
    return sum(int(d) for d in str(n))
# 13. digital_sum(n): Calculates the digital sum of a number, i.e., the sum of its digits until it becomes a single digit.
def digital_sum(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n
# 14. is_pandigital(n, digits): Checks if a number is pandigital, i.e., it contains each digit from 1 to digits exactly once.
def is_pandigital(n, digits):
    num_str = str(n)
    return len(num_str) == digits and set(num_str) == set(str(i) for i in range(1, digits + 1))
#15. collatz_sequence(n): Generates the Collatz sequence starting from a given number n.
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
#16. is_pythagorean_triplet(a, b, c): Checks if the given triplet (a, b, c) forms a Pythagorean triplet, where 
def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2
#17. prime_factors(n): Returns a list of prime factors of a given number n.
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
#18. prime_sieve(n): Returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm.
def prime_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]
#19. prime_count(n): Returns the number of prime numbers up to n using the Sieve of Eratosthenes algorithm. 
def prime_count(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return sum(1 for i in range(n + 1) if sieve[i])
#20. divisors(n): Returns a list of divisors of a given number n.
def divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs
#21. nth_triangle_number(n): Calculates the nth triangle number.
def nth_triangle_number(n):
    return n * (n + 1) // 2
#22. digit_count(n): Counts the number of digits in a given number n.
def digit_count(n):
    return len(str(n))
#23. is_power_of_two(n): Checks if a given number n is a power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
#24. is_permutation(a, b): Checks if two numbers a and b are permutations of each other.
def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))
#25.  totient_function(n): Calculates Euler's totient function (phi function) for a given number n, which counts the positive integers up to n that are relatively prime to n.
def totient_function(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
#26. collatz_length(n): Computes the length of the Collatz sequence starting from a given number n.
def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length
#27. prime_range(start, end): Generates all prime numbers within a given range [start, end].
def prime_range(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
#28. is_pandigital_product(multiplicand, multiplier, product): Checks if a multiplication equation is pandigital, where each digit from 1 to 9 is used exactly once.
def is_pandigital_product(multiplicand, multiplier, product):
    num_str = str(multiplicand) + str(multiplier) + str(product)
    return len(num_str) == 9 and set(num_str) == set("123456789")
#29. is_palindromic_number(n): Checks if a given number n is palindromic.
def is_palindromic_number(n):
    return str(n) == str(n)[::-1]
#30. permutations(iterable, r): Generates all permutations of length r from an iterable.
def permutations(iterable, r=None):
    from itertools import permutations
    return list(permutations(iterable, r))
#31. combinations(iterable, r): Generates all combinations of length r from an iterable.
def combinations(iterable, r):
    from itertools import combinations
    return list(combinations(iterable, r))
#32. product(iterable): Computes the product of all elements in an iterable.
def product(iterable):
    from functools import reduce
    from operator import mul
    return reduce(mul, iterable, 1)
#33. prime_factorization(n): Computes the prime factorization of a given number n and returns it as a dictionary where keys are prime factors and values are their corresponding powers.
def prime_factorization(n):
    factors = {}
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        else:
            divisor += 1
    return factors
#34. proper_divisors_sum(n): Calculates the sum of proper divisors (excluding the number itself) of a given number n.
def proper_divisors_sum(n):
    return sum(divisors(n)[:-1])
#35. prime_pi(n): Computes the prime counting function, which counts the number of prime numbers less than or equal to n.
def prime_pi(n):
    primes = prime_sieve(n)
    return len(primes)
#39.is_circular_prime(n): Checks if a given number n is a circular prime, meaning that all rotations of its digits are prime.
def is_circular_prime(n):
    num_str = str(n)
    rotations = [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))]
    return all(is_prime(rotated) for rotated in rotations)
#40.consecutive_digits_product(n, k): Finds the largest product of k consecutive digits in a given number n.
def consecutive_digits_product(n, k):
    digits = [int(digit) for digit in str(n)]
    max_product = 0
    for i in range(len(digits) - k + 1):
        product = 1
        for j in range(k):
            product *= digits[i + j]
        max_product = max(max_product, product)
    return max_product
#41.next_collatz_number(n): Finds the next number in the Collatz sequence after n
def next_collatz_number(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
#42.reduced_proper_fractions_count(d): Counts the number of reduced proper fractions with denominator d and numerator less than d.
def reduced_proper_fractions_count(d):
    count = 0
    for n in range(1, d):
        if gcd(n, d) == 1:
            count += 1
    return count
#43.nth_permutation(sequence, n): Finds the nth lexicographic permutation of a given sequence.
from itertools import permutations

def nth_permutation(sequence, n):
    return ''.join(next(permutations(sequence, len(sequence))) for _ in range(n - 1))

#44.factorial_digit_sum(n): Calculates the sum of the digits of n!.
def factorial_digit_sum(n):
    fact = factorial(n)
    return sum(int(digit) for digit in str(fact))


#Multiples of 3 and 5
def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
#Even Fibonacci Numbers
def compute():
	ans = 0
	x = 1  # Represents the current Fibonacci number being processed
	y = 2  # Represents the next Fibonacci number in the sequence
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)


if __name__ == "__main__":
	print(compute())

#Largest Prime Factor
import math


# By the fundamental theorem of arithmetic, every integer n > 1 has a unique factorization as a product of prime numbers.
# In other words, the theorem says that n = p_0 * p_1 * ... * p_{m-1}, where each p_i > 1 is prime but not necessarily unique.
# Now if we take the number n and repeatedly divide out its smallest factor (which must also be prime), then the last
# factor that we divide out must be the largest prime factor of n. For reference, 600851475143 = 71 * 839 * 1471 * 6857.
def compute():
	n = 600851475143
	while True:
		p = smallest_prime_factor(n)
		if p < n:
			n //= p
		else:
			return str(n)


# Returns the smallest factor of n, which is in the range [2, n]. The result is always prime.
def smallest_prime_factor(n):
	assert n >= 2
	for i in range(2, math.isqrt(n) + 1):
		if n % i == 0:
			return i
	return n  # n itself is prime


if __name__ == "__main__":
	print(compute())

#Largest Palindrome Product
def compute():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
#Smallest Multiple
#   s  = N(N + 1) / 2.
#   s2 = N(N + 1)(2N + 1) / 6.
# Hence s^2 - s2 = (N^4 / 4) + (N^3 / 6) - (N^2 / 4) - (N / 6).
def compute():
	N = 100
	s = sum(i for i in range(1, N + 1))
	s2 = sum(i**2 for i in range(1, N + 1))
	return str(s**2 - s2)


if __name__ == "__main__":
	print(compute())
	
#10001st Prime
import eulerlib, itertools


# Computers are fast, so we can implement this solution by testing each number
# individually for primeness, instead of using the more efficient sieve of Eratosthenes.
# 
# The algorithm starts with an infinite stream of incrementing integers starting at 2,
# filters them to keep only the prime numbers, drops the first 10000 items,
# and finally returns the first item thereafter.
def compute():
	ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
	return str(ans)


if __name__ == "__main__":
	print(compute())


#Largest product in a series
def compute():
	ans = max(digit_product(NUMBER[i : i + ADJACENT]) for i in range(len(NUMBER) - ADJACENT + 1))
	return str(ans)


def digit_product(s):
	result = 1
	for c in s:
		result *= int(c)
	return result


NUMBER = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
ADJACENT = 13


if __name__ == "__main__":
	print(compute())
	

#Special Pythagorean Triplet
def compute():
	PERIMETER = 1000
	for a in range(1, PERIMETER + 1):
		for b in range(a + 1, PERIMETER + 1):
			c = PERIMETER - a - b
			if a * a + b * b == c * c:
				# It is now implied that b < c, because we have a > 0
				return str(a * b * c)


if __name__ == "__main__":
	print(compute())

#Summation of Primes
import eulerlib


# Call the sieve of Eratosthenes and sum the primes found.
def compute():
	ans = sum(eulerlib.list_primes(1999999))
	return str(ans)


if __name__ == "__main__":
	print(compute())


#Largest Product in a Grid

def compute():
	ans = -1
	width = len(GRID[0])
	height = len(GRID)
	for y in range(height):
		for x in range(width):
			if x + CONSECUTIVE <= width:
				ans = max(grid_product(x, y,  1, 0, CONSECUTIVE), ans)
			if y + CONSECUTIVE <= height:
				ans = max(grid_product(x, y,  0, 1, CONSECUTIVE), ans)
			if x + CONSECUTIVE <= width and y + CONSECUTIVE <= height:
				ans = max(grid_product(x, y,  1, 1, CONSECUTIVE), ans)
			if x - CONSECUTIVE >= -1    and y + CONSECUTIVE <= height:
				ans = max(grid_product(x, y, -1, 1, CONSECUTIVE), ans)
	return str(ans)


def grid_product(ox, oy, dx, dy, n):
	result = 1
	for i in range(n):
		result *= GRID[oy + i * dy][ox + i * dx]
	return result


GRID = [
	[ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
	[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0],
	[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
	[52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
	[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
	[24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
	[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
	[67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
	[24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
	[21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95],
	[78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
	[16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57],
	[86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
	[19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
	[ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
	[88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
	[ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
	[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
	[20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
	[ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48],
]
CONSECUTIVE = 4

#Highly Divisible Triangular Number
import itertools, math


def compute():
	triangle = 0
	for i in itertools.count(1):
		triangle += i  # This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
		if num_divisors(triangle) > 500:
			return str(triangle)


# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
	end = math.isqrt(n)
	result = sum(2
		for i in range(1, end + 1)
		if n % i == 0)
	if end**2 == n:
		result -= 1
	return result


























def compute():
	ans = math.lcm(*range(1, 21))
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
#Sum Square Difference



#Consecutive Prime Sum
import eulerlib


def compute():
	ans = 0
	isprime = eulerlib.list_primality(999999)
	primes = eulerlib.list_primes(999999)
	consecutive = 0
	for i in range(len(primes)):
		sum = primes[i]
		consec = 1
		for j in range(i + 1, len(primes)):
			sum += primes[j]
			consec += 1
			if sum >= len(isprime):
				break
			if isprime[sum] and consec > consecutive:
				ans = sum
				consecutive = consec
	return str(ans)


if __name__ == "__main__":
	print(compute())
#Prime Digit Replacements
import eulerlib


def compute():
	isprime = eulerlib.list_primality(1000000)
	for i in range(len(isprime)):
		if not isprime[i]:
			continue
		
		n = [int(c) for c in str(i)]
		for mask in range(1 << len(n)):
			digits = do_mask(n, mask)
			count = 0
			for j in range(10):
				if digits[0] != 0 and isprime[to_number(digits)]:
					count += 1
				digits = add_mask(digits, mask)
			
			if count == 8:
				digits = do_mask(n, mask)
				for j in range(10):
					if digits[0] != 0 and isprime[to_number(digits)]:
						return str(to_number(digits))
					digits = add_mask(digits, mask)
	raise AssertionError("Not found")


def do_mask(digits, mask):
	return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]


def add_mask(digits, mask):
	return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]


def to_number(digits):
	result = 0
	for d in digits:
		result = result * 10 + d
	return result


if __name__ == "__main__":
	print(compute())

#Permuted Primes
import itertools


def compute():
	cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))
	ans = next(i for i in itertools.count(1) if cond(i))
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
#Combinatoric Selections
import math


def compute():
	ans = sum(1
		for n in range(1, 101)
		for k in range(0, n + 1)
		if math.comb(n, k) > 1000000)
	return str(ans)


if __name__ == "__main__":
	print(compute())

#Lychrel Numbers
def compute():
	ans = sum(1 for i in range(10000) if is_lychrel(i))
	return str(ans)


def is_lychrel(n):
	for i in range(50):
		n += int(str(n)[ : : -1])
		if str(n) == str(n)[ : : -1]:
			return False
	return True


if __name__ == "__main__":
	print(compute())
	
#Powerful Digit Sum
def compute():
	ans = max(sum(int(c) for c in str(a**b))
		for a in range(100) for b in range(100))
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
#Square Root Convergents
def compute():
	LIMIT = 1000
	ans = 0
	numer = 0
	denom = 1
	for _ in range(LIMIT):
		numer, denom = denom, denom * 2 + numer
		# Now numer/denom is the i'th (0-based) continued fraction approximation of sqrt(2) - 1
		if len(str(numer + denom)) > len(str(denom)):
			ans += 1
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
#Spiral Primes
import eulerlib, fractions, itertools


# From the diagram, let's observe the four corners of an n * n square (where n is odd).
# It's not hard to convince yourself that:
# - The bottom right corner always has the value n^2.
# Working clockwise (backwards):
# - The bottom left corner has the value n^2 - (n - 1).
# - The top left corner has the value n^2 - 2(n - 1).
# - The top right has the value n^2 - 3(n - 1).
# Furthermore, the number of elements on the diagonal is 2n - 1.
def compute():
	TARGET = fractions.Fraction(1, 10)
	numprimes = 0
	for n in itertools.count(1, 2):
		for i in range(4):
			if eulerlib.is_prime(n * n - i * (n - 1)):
				numprimes += 1
		if n > 1 and fractions.Fraction(numprimes, n * 2 - 1) < TARGET:
			return str(n)


if __name__ == "__main__":
	print(compute())

#Cubic Permutations
import itertools


def compute():
	numdigits = 0
	data = {}  # str numclass -> (int lowest, int count)
	for i in itertools.count():
		digits = [int(c) for c in str(i**3)]
		digits.sort()
		numclass = "".join(str(d) for d in digits)
		
		if len(numclass) > numdigits:
			# Process and flush data for smaller number of digits
			candidates = [lowest for (lowest, count) in data.values() if count == 5]
			if len(candidates) > 0:
				return str(min(candidates)**3)
			data = {}
			numdigits = len(numclass)
		
		lowest, count = data.get(numclass, (i, 0))
		data[numclass] = (lowest, count + 1)


if __name__ == "__main__":
	print(compute())
	
# Powerful Digit Counts How many n-digit positive integers exist which are also an n th power?
def compute():
	ans = sum(1
		for i in range(1, 10)
		for j in range(1, 22)
		if len(str(i**j)) == j)
	return str(ans)


if __name__ == "__main__":
	print(compute())
	
'''
Project Euler #51

By replacing the first digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the third and fourth digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently, 56003 being the first member of this family, is the smallest prime with this property.

Find the smallest N-digit prime which, by replacing K-digits of the number (not necessarily adjacent digits) with the same digit, is part of an L prime value family.

Note1: It is guaranteed that solution does exist.
Note2: Leading zeros should not be considered.
Note3: If there are several solutions, choose the "lexicographically" smallest one (one sequence is considered "lexicographically" smaller than another if its first element which does not match the corresponding element in another sequence is smaller)

Input Format
Input contains three integers N, K and L.

Output Format
Print the first L numbers of the prime value family found in increasing order.

Constraints
2 ≤ N ≤ 7
1 ≤ K ≤ N
1 ≤ L ≤ 8
'''

import itertools

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def generate_n_digit_primes(N):
    start = 10**(N-1)
    end = 10**N - 1
    all_primes = sieve_of_eratosthenes(end)
    return [p for p in all_primes if p >= start]

def replace_digits_and_check(prime, positions, L):
    prime_str = str(prime)
    family = []
    
    for digit in '0123456789':
        new_number = list(prime_str)
        for pos in positions:
            if new_number[pos] != digit:
                new_number[pos] = digit
        new_number_str = ''.join(new_number)
        if new_number_str[0] != '0' and is_prime(int(new_number_str)):
            family.append(int(new_number_str))
    
    if len(family) >= L:
        return sorted(family)[:L]
    
    return []

def find_smallest_prime_family(N, K, L):
    primes = generate_n_digit_primes(N)
    
    for prime in primes:
        prime_str = str(prime)
        indices = list(range(len(prime_str)))
        
        for positions in itertools.combinations(indices, K):
            prime_family = replace_digits_and_check(prime, positions, L)
            if prime_family:
                return prime_family
    
    return []

# Input
N, K, L = map(int, input().split())

# Find and print the result
result = find_smallest_prime_family(N, K, L)
print(' '.join(map(str, result)))



""""
1
def calcular_valor_neto(salario_base, horas_extras, bonificaciones):

    # Calcular el valor de las horas extras
    valor_horas_extras = horas_extras * (salario_base / 192)* 1.25

    # Calcular el valor de las bonificaciones
    valor_bonificaciones = bonificaciones * 0.05 * salario_base

    # Calcular el valor neto a pagar
    valor_neto = salario_base + valor_horas_extras + valor_bonificaciones

    salario_total = valor_neto * 0.915

    return salario_total

# Obtener los parámetros del usuario
entrada = input("Ingrese los parámetros (salario_base horas_extras bonificaciones): ")
parametros = entrada.split()

# Convertir los parámetros a los tipos de datos adecuados
salario_base = float(parametros[0])
horas_extras = int(parametros[1])
bonificaciones = int(parametros[2])

# Calcular y mostrar el valor neto a pagar
valor_neto = calcular_valor_neto(salario_base, horas_extras, bonificaciones)
print("Valor neto a pagar:", valor_neto)


//////////////////////////////////////////////////////////////////////////////////////////
2
def check_password_security(password):
    # Check password length
    if len(password) < 6:
        return 6 - len(password)

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return 1

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return 1

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return 1

    # Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[]{}|\\;:'\",.<>/?"
    if not any(char in special_characters for char in password):
        return 1

    return 0

# Get password length and password from user
length = int(input("Enter password length: "))
password = input("Enter password: ")

# Check password security and print the minimum number of characters to add
security_score = check_password_security(password)
print("Minimum number of characters to add:", security_score)

//////////////////////////////////////////////////////////////////////////////////////////
3
3
El programa recibe tres enteros X, Y y N. N representa el número de bloques de código, tal que cada bloque Ni impreso en la salida representa un número entre 1 y N. Para cada Ni de 1 a N, si Ni es divisible por X, se imprime EC en lugar del número; si Ni es divisible por Y, se imprime EI en lugar del número. Si es divisible por X y Y, se imprime ECEI. Si no es divisible por ninguno, se imprime el número.
def print_numbers(X, Y, N):
    for i in range(1, N+1):
        if i % X == 0 and i % Y == 0:
            print("ECEI")
        elif i % X == 0:
            print("EC")
        elif i % Y == 0:
            print("EI")
        else:
            print(i)

entrada = input()
parametros = entrada.split()

# Convertir los parámetros a los tipos de datos adecuados
X = int(parametros[0])
Y = int(parametros[1])
N = int(parametros[2])



# Print the numbers based on the given conditions
print_numbers(X, Y, N)

//////////////////////////////////////////////////////////////////////////////////////////
4
La primera línea recibirá un número N equivalente al número de registros a continuación. Cada línea es un registro formado por 5 números separados por espacios que representan número de baños, número de habitaciones, tiempo promedio para llegar al trabajo, número de parques cercanos, valor de la casa. La casa debe cumplir con mínimo 2 baños, mínimo 4 habitaciones, tiempo menor a 35, mínimo 4 parques. Si cumple, imprime el precio; de lo contrario, no imprime. Si ninguna cumple, imprime NO DISPONIBLE.
def check_house_availability(registros):
    casas_disponibles = []  # Lista para almacenar los valores de las casas disponibles
    for registro in registros:
        datos = registro.split()
        num_banos = int(datos[0])
        num_habitaciones = int(datos[1])
        tiempo_trabajo = int(datos[2])
        num_parques = int(datos[3])
        valor_casa = int(datos[4])

        if num_banos >= 2 and num_habitaciones >= 4 and tiempo_trabajo < 35 and num_parques >= 4:
            casas_disponibles.append(valor_casa)  # Agregar el valor de la casa a la lista de casas disponibles

    if casas_disponibles:
        for casa in casas_disponibles:
            print(casa)
    else:
        print("NO DISPONIBLE")


# Get the number of records
N = int(input("Enter the number of records: "))

# Read the records
registros = []
for _ in range(N):
    registro = input("Enter a record: ")
    registros.append(registro)

# Check house availability and print the price if available
check_house_availability(registros)

//////////////////////////////////////////////////////////////////////////////////////////
6

def reorganize_teams(N, identifiers):
    sorted_identifiers = sorted(identifiers)
    
    if identifiers == sorted_identifiers:
        print("Sin cambios")
    elif identifiers[::-1] == sorted_identifiers:
        start_index = identifiers.index(sorted_identifiers[0]) + 1
        end_index = identifiers.index(sorted_identifiers[-1]) + 1
        if  start_index - end_index == 1:
            print("Intercambiar", end_index, start_index)
        else:
            print("Reversar", end_index, start_index)
    else:
        for i in range(len(identifiers)-1):
            if identifiers[i] != sorted_identifiers[i]:
                start_index = i + 1
                end_index = identifiers.index(sorted_identifiers[i]) + 1
                identifiers[start_index-1:end_index] = identifiers[start_index-1:end_index][::-1]
                if identifiers == sorted_identifiers:
                    if end_index - start_index == 1:
                        print("Intercambiar", start_index, end_index)
                    else:
                        print("Reversar", start_index, end_index)
                    break
        else:
            print("No tocar")

# Get the number of elements
N = int(input("Enter the number of elements: "))

# Get the list of identifiers
identifiers = input("Enter the list of identifiers separated by space: ").split()

# Call the reorganize_teams function
reorganize_teams(N, identifiers)

"""
