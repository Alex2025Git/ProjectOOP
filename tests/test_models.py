import pytest

from src.models import Product


# вызываем тест-функцию для проверки получения маски номера карты
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            [
                "Samsung Galaxy C23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ],
        )
    ],
)
def test_class_product(value, expected):
    assert Product(**value).name == expected[0]
    assert Product(**value).description == expected[1]
    assert Product(**value).price == expected[2]
    assert Product(**value).quantity == expected[3]


def test_init_product(smartphone_data):
    assert smartphone_data.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_data.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_data.price == 180000.0
    assert smartphone_data.quantity == 5


def test_init_category(smartphone_category, smartphone_data):
    assert smartphone_category.name == "Смартфоны"
    assert smartphone_category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert smartphone_category.products[0].name == smartphone_data.name
    assert smartphone_category.products[0].description == smartphone_data.description
    assert smartphone_category.products[0].price == smartphone_data.price
    assert smartphone_category.products[0].quantity == smartphone_data.quantity
    assert smartphone_category.category_count == 1
    assert smartphone_category.product_count == 1
