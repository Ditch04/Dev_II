from Fractions import Fraction

if __name__ == "__main__":

    frac1 = Fraction(1, 4)
    frac2 = Fraction(12, 8)
    frac3 = Fraction(-1, 6)
    frac4 = Fraction(1, 3)

    try:
        frac = Fraction(2, 0)
        print(frac)
    except ZeroDivisionError as e:
        print(e)

    try:
        frac = Fraction(2, 4)
        print(frac + 's')
    except TypeError as e:
        print(e)

    print(str(frac1) + "\n")
    print(frac1.as_mixed_number() + "\n")
    print(frac2.as_mixed_number() + "\n")
    print(str(frac2) + "\n")

    try:
        frac = 'bonjour'
        print(frac1 - frac)
    except TypeError as e:
        print(e)

    try:
        frac = Fraction(3, 0)
        print(frac * frac2)
    except ZeroDivisionError as e:
        print(e)

    print(f"{frac1} + {frac2} = {frac1 + frac2}\n")

    print(f"{frac2} - {frac1} = {frac2 - frac1}\n")

    print(f"{frac1} * {frac2} = {frac1 * frac2}\n")

    print(f"{frac1} / {frac2} = {frac1 / frac2}\n")

    print(f"{frac1 ** 2}\n")

    print(f"{frac1 == frac2}\n")

    print(f"{float(frac1)}\n")

    print(frac1.is_adjacent_to(frac4))

    print(Fraction(1, 2) + Fraction(-1, 2))