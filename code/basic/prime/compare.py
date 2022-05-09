import prime, example_py_cy
import time
print("===Check the accuracy===")
print(f'Are they equal? {prime.primes(1000) == example_py_cy.primes_python_compile(1000)}')

print("====Compare the time===")
# cython
t1 = time.time()
prime.primes(1000)
t2 = time.time()
print(f"Cython = {t2 - t1} sec")

# python
t3 = time.time()
example_py_cy.primes_python_compile(1000)
t4 = time.time()
print(f"python = {t4 - t3} sec")
