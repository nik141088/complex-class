import math
import pytest
from my_complex import Complex


def test_addition_commutativity_with_real():
    for a in [1, 2, -1.5, 0]:
        for b in [0, 1, -1, 2.5]:
            for c in [1, -2.5, 0]:
                z1 = Complex(a, b)
                assert z1 + c == c + z1

def test_exponentiation_property():
    for a in [1, 2, 0.5, -1.5]:
        for b in [0, 1, -1, 2.5]:
            z = Complex(a, b)
            for p in [2, 0.5, -1, 3]:
                for q in [0, 1, -1, 2.5]:
                    z1 = (z ** p) ** q
                    z2 = (z ** q) ** p
                    z3 = z ** (p * q)
                    assert abs(z1.to_polar()[0] - z2.to_polar()[0]) < 1e-3
                    assert abs(z1.to_polar()[0] - z3.to_polar()[0]) < 1e-3
                    
def test_addition():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)
    assert z1 + z2 == Complex(4, 6)
    assert z1 + 3 == Complex(4, 2)
    assert 3 + z1 == Complex(4, 2)

def test_subtraction():
    z1 = Complex(5, 6)
    z2 = Complex(1, 2)
    assert z1 - z2 == Complex(4, 4)
    assert z1 - 2 == Complex(3, 6)
    assert 2 - z1 == Complex(-3, -6)

def test_multiplication():
    z1 = Complex(1, 1)
    z2 = Complex(2, 3)
    assert z1 * z2 == Complex(-1, 5)
    assert z1 * 2 == Complex(2, 2)
    assert 2 * z1 == Complex(2, 2)

def test_division():
    z1 = Complex(1, 1)
    z2 = Complex(1, -1)
    assert z1 / z2 == Complex(0, 1)
    assert z1 / 2 == Complex(0.5, 0.5)
    assert 2 / z1 == Complex(1, -1)

def test_conjugate():
    z = Complex(1, 1)
    assert z.conjugate() == Complex(1, -1)

def test_absolute():
    z = Complex(3, 4)
    assert abs(z) == 5

def test_phase():
    z = Complex(1, 1)
    assert z.phase() == pytest.approx(math.pi / 4, rel=1e-10)

def test_polar_conversion():
    z = Complex(1, 1)
    r, theta = z.to_polar()
    assert r == pytest.approx(math.sqrt(2), rel=1e-10)
    assert theta == pytest.approx(math.pi / 4, rel=1e-10)
    assert z == Complex.from_polar(r, theta)

def test_equality():
    z1 = Complex(1, 1)
    z2 = Complex(1, 1)
    z3 = Complex(1, -1)
    assert z1 == z2
    assert z1 != z3
    assert -z1 == -z2



test_addition_commutativity_with_real()
test_exponentiation_property() # fail
test_addition()
test_subtraction()
test_multiplication()
test_division()
test_conjugate()
test_absolute()
test_phase()
test_polar_conversion()
test_equality()
