# cython: language_level=3
import pyximport
pyximport.install()

import prime
print(prime.primes(10))