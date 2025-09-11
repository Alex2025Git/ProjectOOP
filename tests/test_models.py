import pytest

from src.models import CategoryIterator, LawnGrass, Product, Smartphone


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
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert smartphone_category.products == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n"
    assert smartphone_category.category_count == 1
    assert smartphone_category.product_count == 1

    smartphone_category.add_product(smartphone_data)
    assert smartphone_category.product_count == 2


def test_new_product(smartphone_data, smartphone_category):
    new_product = smartphone_data.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 190000.0,
            "quantity": 5,
        },
        [smartphone_data],
    )

    assert new_product.name == smartphone_data.name
    assert new_product.description == smartphone_data.description
    assert new_product.price == 180000
    assert new_product.quantity == 10
    for i in CategoryIterator(smartphone_category):
        assert i.name == "Samsung Galaxy S23 Ultra"

    smartphone_category.add_product(
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    )
    assert smartphone_category.product_count == 4

    smartphone_category.add_product(
        LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    )
    assert smartphone_category.product_count == 5

    try:
        smartphone_category.add_product("Некорректные данные")
    except TypeError:
        print("Тест пройден, передан некорректный класc объекта")


def test_add_product(smartphone_data_add):
    assert smartphone_data_add[0] + smartphone_data_add[1] == 2580000
    try:
        smartphone_data_add[2] + smartphone_data_add[4]
    except TypeError:
        print("Тест пройден, передан некорректный класc объекта")
