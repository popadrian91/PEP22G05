class Haine:

    def __init__(self, nume, pret, stoc, **kwargs):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc

    def __str__(self):
        f = f"\n -------------- " \
            f"\n{self.__class__.__name__} " \
            f"\n -------------- " \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}"
        return f


class Accesorii:

    def __init__(self, nume, pret, stoc,material='aur'):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc
        self.material = material

    def __str__(self):
        f = f"\n -------------- " \
            f"\n{self.__class__.__name__} " \
            f"\n -------------- " \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}" \
            f"\n Material = {self.material}"
        return f


if __name__ == '__main__':
    bluze = Haine('tricou', 3, 4)
    print(bluze.nume, bluze.pret, bluze.stoc)
    cercei = Accesorii('Cercei', 'Aur', 4, 5)
    print(cercei.nume, cercei.material, cercei.pret, cercei.stoc)

    print(str(bluze))
    print(str(cercei))
