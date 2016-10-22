import pytest
from fraction import *

def test_raises_when_denominator_is_zero():
#    with pytest.raises(ValueError):
#        Fraction(10, 0)
"""    


def test_is_proper_when_absolute_numerator_is_smaller_than_absolute_denominator():
    proper_fraction = Fraction(3, -5)
    
    is_proper = proper_fraction.proper
    
    assert is_proper


def test_is_improper_when_absolute_numerator_is_greater_or_equal_to_absolute_denominator():
    improper_fraction = Fraction(-5, 3)
    
    is_proper = improper_fraction.proper
    
    assert not is_proper


"""
def test_reduce_returns_same_fraction_when_fraction_is_irreducible():
#    irreducible_fraction = Fraction(3, -5)
#    
#    reduced_fraction = irreducible_fraction.reduce()
#
#    assert reduced_fraction.numerator == irreducible_fraction.numerator
#    assert reduced_fraction.denominator == irreducible_fraction.denominator


def test_reduced_fraction_has_different_numerator_and_denominator_when_fraction_is_reducible():
#    reducible_fraction = Fraction(2*3, 2*-5)
#    
#    reduced_fraction = reducible_fraction.reduce()
#
#    assert reduced_fraction.numerator != reducible_fraction.numerator
#    assert reduced_fraction.denominator != reducible_fraction.denominator


# Test and implement Fraction.__eq__ and refactor the assertions in the last two tests

