from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс, который становится родительским для класса  Product."""

    def __init__(self, name: str, description: str, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity

    @classmethod
    @abstractmethod
    def new_product(cls, data_product: dict, list_products=None):
        pass
