import pytest
import base64
from src.extractor import extract_data

def test_does_not_return_empty_list():
    result = extract_data("samples/sample.pdf")
    assert isinstance(result, list)
    assert len(result) > 0

def test_returns_list_of_strings():
    result = extract_data("samples/sample.pdf")
    assert all(isinstance(item, str) for item in result)

def test_returns_valid_base64():
    result = extract_data("samples/sample.pdf")
    for item in result:
        try:
            base64.b64decode(item)
        except Exception:
            pytest.fail(f"Item is not valid base64: {item}")
