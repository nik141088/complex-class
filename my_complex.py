import math

SIGNIFICANCE_DIGITS = 10
EPSILON = 10 ** -SIGNIFICANCE_DIGITS # 1e-10

def is_close(num1, num2):
    if math.isinf(num1) and math.isinf(num2):
        return True
    return abs(num1 - num2) < EPSILON

def is_zero(num1):
    return is_close(num1, 0)

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class Complex:

    def __init__(self, real, img=0.0):
        self.real = round(real, SIGNIFICANCE_DIGITS)
        self.img = round(img, SIGNIFICANCE_DIGITS)
    
    def __str__(self):
        return (
            f'{self.real}' if is_zero(self.img) else
            f'{self.img}i' if is_zero(self.real) else
            f'{self.real} + {self.img}i'
        )

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Complex):
            return is_close(self.real, other.real) and is_close(self.img, other.img)
        else:
            return is_close(self.real, other) and is_zero(self.img)

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.img + other.img)
        else:
            return Complex(self.real + other, self.img)

    def __radd__(self, other):
        # called as other + self when other is not Complex
        return self + other

    def __neg__(self):
        return Complex(-self.real, -self.img)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        # called as other - self when other is not Complex
        return self - other

    def __abs__(self):
        return math.sqrt(self.real**2 + self.img**2)

    def phase(self):
        # theta = arctan (b/a) where z = a + i.b
        if self == 0 or self == Complex(math.inf, math.inf):
            return math.nan
        else:
            return math.atan2(self.img, self.real)

    def to_polar(self):
        r = abs(self)
        theta = self.phase()
        return r, theta

    @staticmethod
    def from_polar(r, theta):
        return Complex(
            r * math.cos(theta),
            r * math.sin(theta)
        )

    @staticmethod
    def real_power(z1, power):
        r, theta = z1.to_polar()
        r_pow = r ** power  # power
        theta_pow = theta * power  # multiplication
        return Complex.from_polar(r_pow, theta_pow)

    @staticmethod
    def complex_power(z1, z2):
        # Let z1 = polar(r, theta) and z2 = c + di. After some algebra, we can find:
        # z1 ** z2 = polar(r**c * e**(-d*theta), c*theta + d*ln(r))
        r, theta = z1.to_polar()
        r_complex_pow = (r ** z2.real) * math.exp(-z2.img * theta)
        theta_complex_pow = z2.real * theta + z2.img * math.log(r)
        return Complex.from_polar(r_complex_pow, theta_complex_pow)

    def __pow__(self, power):
        if isinstance(power, Complex):
            return Complex.complex_power(self, power)
        else:
            return Complex.real_power(self, power)

    def __rpow__(self, other):
        # called as other ** self when other is not Complex
        return Complex(other) ** self

    def __mul__(self, other):
        if isinstance(other, Complex):
            # z1 = r1 * (cos t1 + i.sin t1); z2 = r2 * (cos t2 + i.sin t2)
            # z3 = z1*z2 = r1r2 * (cos t1 cos t2 + ii sin t1 sin t2 + i cos t1 sin t2 + i cos t2 sin t1)
            # z3 = r1r2 * (cos (t1+t2) + i sin (t1 + t2)
            r1, theta1 = self.to_polar()
            r2, theta2 = other.to_polar()
            r_combined = r1 * r2
            theta_combined = theta1 + theta2
            return Complex.from_polar(r_combined, theta_combined)
        else:
            return Complex(self.real * other, self.img * other)
    
    def __rmul__(self, other):
        # called as other * self when other is not Complex
        return self * other

    def conjugate(self):
        return Complex(self.real, -self.img)

    def __truediv__(self, other):
        # z1/z2 = z1 * (1/z2) = z1 * z2**-1
        if other == 0:
            raise ZeroDivisionError(f"Can't divide by {other}")
        else:
            return self * (other ** -1)

    def __rtruediv__(self, other):
        # cases where the left operand is not complex.
        # Here we are actually doing `other / self` where other is not Complex
        return Complex(other) / self

