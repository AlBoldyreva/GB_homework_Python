from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence

    def __str__(self):
        return f'Пальто: размер {self.size}, расход ткани {self.expence}, общий расход ткани на пальто {Coat.expence_count:.02f}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.expence_count += self.expence

    def __str__(self):
        return f'Костюм: рост {self.height}, расход ткани {self.expence}, общий расход ткани на костюмы {Suit.expence_count:.02f}'

    @property
    def expence(self):
        exp = self.height * 2 + 0.3
        return float(f'{exp:.02f}')

cloth1 = Coat(55)
cloth2 = Coat(64)
print(cloth1)
print(cloth2)

cloth3 = Suit(174)
cloth4 = Suit(180)
print(cloth3)
print(cloth4)