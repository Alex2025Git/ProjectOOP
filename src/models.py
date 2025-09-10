from numpy.ma.core import count


class Product:
    """Класс с данными о продукте"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {round(self.price)} руб. Остаток: {self.quantity} шт.'
        #Название продукта, 80 руб. Остаток: 15 шт.

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return print("Необходимо передать объект класса Product")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_input = input(
                    'Цена товара понижается.\nВведите "y" для подтверждения: '
                )
                if user_input.lower() == "y":
                    self.__price = new_price

    @classmethod
    def new_product(cls, data_product: dict, list_products=None):
        if list_products is None:
            list_products = []
        name :str = data_product.get("name")
        description :str  = data_product.get("description")
        price :float  = data_product.get("price")
        quantity :int  = data_product.get("quantity")

        for i in list_products:
            old_price = i.price
            if i.name == name:
                i.quantity += quantity
                max_price = max(price, old_price)
                i.price = max_price
                return i
        return cls(name, description, price, quantity)


class Category:
    """Класс с данными о категории продуктов"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def __str__(self):
        sum_quantity = 0
        for i in self.__products:
            sum_quantity += i.quantity
        return f'{self.name}, количестов продуктов: {sum_quantity} шт.'
    #Название категории, количество продуктов: 200 шт.

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        str_product = ""
        for i in self.__products:
            str_product += (
                f"{i.name}, {round(i.price)} руб. Остаток: {i.quantity} шт.\n"
            )
        return str_product

    @property
    def product_in_list(self):
        new_list = []
        for i in self.__products:
            new_list.append(i)
        return new_list

class CategoryIterator:

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.product_in_list):
            product = self.category.product_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

