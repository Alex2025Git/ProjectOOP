import os
from unittest.mock import patch

from src.reading_files import reading_json


@patch("json.load")
def test_reading_json(mock_get, list_category):
    mock_get.return_value = list_category
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, '..', 'data', 'products.json')
    assert reading_json(file)[0].name == list_category[0].get("name")
