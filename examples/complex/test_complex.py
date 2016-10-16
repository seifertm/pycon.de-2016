from complex import *

def test_add_returns_sum_of_coefficients():
    augend = Complex(4,  2)
    addend = Complex(5, -9)
    
    complex_sum = augend + addend
    
    assert complex_sum.real == augend.real + addend.real
    assert complex_sum.imaginary == augend.imaginary + addend.imaginary


def test_sub_returns_difference_of_coefficients():
    minuend = Complex(4, 2)
    subtrahend = Complex(5, -9)
    
    difference = minuend - subtrahend
    
    assert difference.real == minuend.real - subtrahend.real
    assert difference.imaginary == minuend.imaginary - subtrahend.imaginary


def test_mul_returns_product_of_coefficients():
    multiplier = Complex(4, 2)
    multiplicand = Complex(5, -9)
    
    product = multiplier * multiplicand
    
    assert product.real == multiplier.real * multiplicand.real - multiplier.imaginary * multiplicand.imaginary
    assert product.imaginary == multiplier.real * multiplicand.imaginary + multiplier.imaginary * multiplicand.real


def test_conjugate_has_inverted_imaginary_coefficient():
    comp = Complex(4, 2)
    
    conjugate = comp.conjugate()
    
    assert conjugate.imaginary == -comp.imaginary


# What about commutated operations?

# Refactor tests by implementing Complex.__eq__ using TDD
