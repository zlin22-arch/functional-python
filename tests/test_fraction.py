from Fraction import Fraction

num0 = Fraction(0,1)
num1 = Fraction(1,1)
num1b = Fraction(10,10)
num2 = Fraction(2,1)

def test_equals_1():
    assert num1 == num1

def test_equals_2():
    assert num1 == num1b

def test_equals_3():
    assert num1 != num2

def test_add_1():
    assert num1 + num2 == num2 + num1

def test_add_2():
    assert num1 + num0 == num1

def test_add_3():
    assert num1 + num1 == num2

def test_mul_1():
    assert num1 * num0 == num0

def test_mul_2():
    assert num1 * num0 == num0

def test_mul_3():
    assert num1 * num1 == num1b
