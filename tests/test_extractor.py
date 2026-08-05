import pytest
from src.extractor import extract_data
import json

def test_returns_a_string():
    result = extract_data("samples/sample.pdf")
    assert isinstance(result, str)

def test_returns_valid_json():
    result = extract_data("samples/sample.pdf")
    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        pytest.fail("Result is not valid JSON")

    expected_keys = {
        "date",
        "vendor",
        "description",
        "purchase_order_number",
        "part_number",
        "who_ordered_it",
        "doc_type"
    }
    assert set(data.keys()) == expected_keys
