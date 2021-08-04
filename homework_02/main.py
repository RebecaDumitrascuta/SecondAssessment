
# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# ○ __init__ : instanțiem numărător și numitor
# ○ __str__ : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea
# ○ inverse: returnează o nouă fracție (inversa fracției)



class Fraction:
    def __init__(self, counter, denominator):
        print ('This is the constructor of Fraction Class')
        self.counter = counter
        self.denominator = denominator
    # def __str__(self):
    #     return f'Object of type{type(self)} with counter = '{self.counter}'
    #     print(counter, '/', denominator)

    @property
    def counter(self):
        return self._counter


    @counter.setter
    def counter(self, counter):
        self._counter = counter

    @counter.deleter
    def counter(self):
        self._counter

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def counter(self, denominator):
        self.denominator = denominator

    @denominator.deleter
    def counter(self):
        self._denominator

if __name__ == '__main__':
    counter = Fraction(counter)
    print(counter)



