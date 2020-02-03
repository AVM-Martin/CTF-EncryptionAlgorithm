from random import randint

from RSA import constants


def extended_euclid(a, b):
	if b == 0:
		return a, 1, 0

	result, x, y = extended_euclid(b, a % b)
	return result, y, x - (a // b) * y


def fast_exponentiation(a, p, mod):
	if p == 0:
		return 1

	result = fast_exponentiation(a, p // 2, mod)
	result = (result * result) % mod

	if p % 2 == 1:
		result = (result * a) % mod

	return result


def is_probably_prime(a, d, r, number):
	a = fast_exponentiation(a, d, number)

	if a == 1:
		return True

	for i in range(r):
		if i > 0:
			a = (a * a) % number

		if a == number - 1:
			return True

	return False


def is_prime(number):
	d = number - 1
	r = 0

	while d % 2 == 0:
		d //= 2
		r += 1

	for i in range(constants.ITERATION):
		a = randint(2, number - 2)
		if not is_probably_prime(a, d, r, number):
			return False

	return True


def get_prime():
	while True:
		result = randint(constants.MIN_PRIME, constants.MAX_PRIME)

		if is_prime(result):
			break

	return result
