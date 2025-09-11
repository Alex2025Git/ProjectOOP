import os
from unittest.mock import patch

from src.reading_files import reading_json


@patch("json.load")
def test_reading_json(mock_get, list_category):
    mock_get.return_value = list_category
    assert reading_json(os.path.abspath("data/products.json"))[0].name == list_category[0].get("name")
