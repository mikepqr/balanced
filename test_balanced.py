import pytest

from balanced import balanced, simple_balanced

inputs = [
    ('()', True),
    ('(())', True),
    ('()()', True),
    ('(()()())()', True),
    ('((()', False),
    ('()))', False),
    (')(', False)
]


@pytest.mark.parametrize("s, is_balanced", inputs)
def test_balanced(s, is_balanced):
    assert balanced(s) == (s if is_balanced else False)


@pytest.mark.parametrize("s, is_balanced", inputs)
def test_simple_balanced(s, is_balanced):
    assert simple_balanced(s) == is_balanced
