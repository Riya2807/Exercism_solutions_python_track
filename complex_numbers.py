from math import cos, sin, exp
def _make_complex(number):
    if not isinstance(number,ComplexNumber):
        number = ComplexNumber(number,0)
    return number
    
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        pass
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
        pass
    def __add__(self, other):
        other = _make_complex(other)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        pass
    def __radd__(self, other):
        return self + other
        
    def __mul__(self, other):
        other = _make_complex(other)
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),(self.imaginary * other.real + self.real * other.imaginary))
        pass
    def __rmul__(self, other):
        return self*other
    def __sub__(self, other):
        other = _make_complex(other)
        return ComplexNumber((self.real - other.real),   (self.imaginary - other.imaginary))
        pass
    def __rsub__(self,other):
        return (self*-1) + other
    def __truediv__(self, other):
        other = _make_complex(other)
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary)/(other.real**2 + other.imaginary**2), (other.real * self.imaginary - self.real * other.imaginary)/(other.real**2 + other.imaginary**2))
        pass
    def __rtruediv__(self, other):
        other = _make_complex(other)
        return other / self
    def __abs__(self):
        return pow(self.real ** 2 + self.imaginary ** 2, 0.5)
        pass
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
        pass
    def exp(self): 
        return ComplexNumber(round(cos(self.imaginary), 8) * exp(self.real), round(sin(self.imaginary), 8) * exp(self.real))
        pass
