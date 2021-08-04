# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# ○ __init__ : instanțiem numărător și numitor
# ○ __str__ : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea
# ○ inverse: returnează o nouă fracție (inversa fracției)

class Fraction:
    def __init__(self, cont, denominator):
        self.cont = cont
        self.denominator = denominator

    def __str__(self):
        return 'This is ' + str(self.cont) + '/' + str(self.denominator)

    def __add__(self):
        return self.cont + self.denominator

    def __sub__(self):
        return self.cont - self.denominator

    def inverse(self):
        return self.denominator / self.cont


if __name__ == '__main__':
    obj_01 = Fraction(cont=10, denominator=2)
    print(obj_01)
    print(obj_01.__add__())
    print(obj_01.__sub__())
    print(obj_01.inverse())
