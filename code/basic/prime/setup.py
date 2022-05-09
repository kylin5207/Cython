# cython: language_level=3

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["prime.pyx", "example_py_cy.py"], annotate=True)
)