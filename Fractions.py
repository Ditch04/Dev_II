def gcd(a, b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while x % y != 0:
        r = x % y
        x = y
        y = r
    return y


class Fraction:
    """Class representing a fraction and operations on it

    Author : Dylan Feron
    Date : November 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num and den must be integers
        POST : creates a fraction object where the numerator is the first param and the denominator the second param
        RAISES : ZeroDivisionError if den == 0
        """
        if den == 0:
            raise ZeroDivisionError("The denominator can't be equal to zero \n")

        if num < 0:
            den = -den
            num = -num

        if num == 0:
            self.__num = 0

        else:
            num, den = self.simplify(num, den)
        self.__num = num
        self.__den = den

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    @staticmethod
    def simplify(a, b):
        com_div = gcd(a, b)
        a /= com_div
        b /= com_div
        return int(a), int(b)

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : /
        POST : returns a fraction in string format
        """
        if self.denominator == 1:
            return str(self.numerator)

        elif self.numerator == 0:
            return '0'

        else:
            return f'{self.numerator}/{self.denominator}'

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : /
        POST : returns a string of the reduced fraction as a mixed number (ex : 1 1/2)
        """
        integer = self.numerator // self.denominator
        if integer == 0:
            print("the fraction is a proper fraction \n")
            return self.__str__()
        rest = self.numerator % self.denominator
        if rest == 0:
            return str(integer)
        return f"{integer} + {rest}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : -
         POST : returns the sum of self and other as a new fraction object
         RAISE : TypeError if one of the argument is not a fraction object
         """
        if isinstance(other, Fraction):
            add_num = self.numerator * other.denominator + self.denominator * other.numerator
            add_den = self.denominator * other.denominator
            return Fraction(add_num, add_den)

        else:
            raise TypeError("One or both of the arguments are not fraction \n")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : /
        POST : returns a new fraction object from the result of the subtraction between self and other
        RAISE : TypeError if one of the argument is not a fraction object
        """
        if isinstance(other, Fraction):
            sub_num = self.numerator * other.denominator - self.denominator * other.numerator
            sub_den = self.denominator * other.denominator
            return Fraction(sub_num, sub_den)

        else:
            raise TypeError("One or both of the arguments are not fraction \n")

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :
        POST : returns a new fraction object from the result of the multiplication between self and other
        RAISE : TypeError if one of the argument is not a fraction object
        """
        if isinstance(other, Fraction):
            mul_num = self.numerator * other.numerator
            mul_den = self.denominator * other.denominator

            return Fraction(mul_num, mul_den)

        else:
            raise TypeError("One or both of the arguments are not fraction \n")

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : /
        POST : returns a new fraction object from the result of the division between self and other
        RAISE : TypeError if one of the argument is not a fraction
                ZeroDivisionError if the numerator of other is 0
        """
        if isinstance(other, Fraction):
            if other.denominator == 0:
                raise ZeroDivisionError("The denominator can't be equal to zero \n")
            else:
                div_num = self.numerator * other.denominator
                div_den = self.denominator * other.numerator

            return Fraction(div_num, div_den)

        else:
            raise TypeError("One or both of the arguments are not fraction \n")

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other must be an integer
        POST : Returns a new fraction object as the power of the fraction in param
        """
        if other.numerator == 0:
            return Fraction(1, 1)

        else:
            pow_num = pow(self.numerator, other)
            pow_den = pow(self.denominator, other)

            return Fraction(pow_num, pow_den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : Both arguments must be fraction objects
        POST : Returns True if the fractions are equals (in their simplified form, their num and den are equals)
        RAISE : /
        """

        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : /
        POST : Returns the decimal value of the fraction (1/2 -> 0.5)
        """
        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : Returns True if the value of the fraction is zero
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : Returns True if the fraction is an integer
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : return True if the absolute value of the fraction is < 1
        """
        return abs(self.numerator / self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : Returns True if the numerator is 1
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : Both arguments must be fraction objects
        POST : Returns True if the difference between both fractions is a unit
        RAISES : /
        """

        frac = self.__sub__(other)
        return frac.numerator == 1




