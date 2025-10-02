class PrintMixin:
    def __init__(self):
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
