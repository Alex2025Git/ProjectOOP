import pytest

from src.models import Category, Product


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
            "Samsung Galaxy C23 Ultra",
        )
    ],
)
def test_class_product(value, expected):
    assert Product(**value).name == expected


# вызываем тест-функцию для проверки получения маски номера карты
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
                "станет вашим другом и помощником",
                "products": [
                    {
                        "name": '55" QLED 4K',
                        "description": "Фоновая подсветка",
                        "price": 123000.0,
                        "quantity": 7,
                    }
                ],
            },
            1,
        )
    ],
)
def test_class_category(value, expected):
    assert Category(**value).category_count == expected
