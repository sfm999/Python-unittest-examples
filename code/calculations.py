
class Calculations:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def get_sum(self) -> int:
        return self.a + self.b
    
    def get_difference(self):
        return self.a - self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_quotient(self):
        return self.a / self.b