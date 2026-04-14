import pytest

from src.main import reverse_string


@pytest.mark.parametrize(
    "string, reversed_result", [("hello", "olleh"), ("world", "dlrow"), ("12345", "54321"), ("", "")]
)
def test_reverse_string(string, reversed_result):
    assert reverse_string(string) == reversed_result
