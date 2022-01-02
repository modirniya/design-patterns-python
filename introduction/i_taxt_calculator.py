class ITaxCalculator:
    def calculate_tax(self) -> float:
        raise NotImplementedError


class TaxCalculator2019(ITaxCalculator):
    def calculate_tax(self) -> float:
        print('calculated')
