import pytest
from src.extractor import extract_data

def test_does_not_return_empty_list():
    result = extract_data("samples/sample.pdf")
    assert isinstance(result, list)
    assert len(result) > 0
