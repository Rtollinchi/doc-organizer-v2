import pytest
from src.extractor import extract_data

def test_does_not_return_empty_list():
    result = extract_data("samples/sample.pdf")
    assert isinstance(result, list)
    assert len(result) > 0

def test_returns_list_of_strings():
    result = extract_data("samples/sample.pdf")
    assert all(isinstance(item, str) for item in result)
