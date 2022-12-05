import pytest
from pizzeria import log, bake, delivery, pickup


@pytest.mark.parametrize(
    'template, expected',
    [
        ('{func_name}', 'my_func'),
        ('{func_result}', 'Hello, world!'),
        ]
    )
def test_log_func_name(template, expected):
    @log(template)
    def my_func(x: str) -> str:
        return x
    assert my_func('Hello, world!') == expected


def test_bake():
    assert 'Приготовили за' in bake(None)


def test_delivery():
    assert 'Доставили за' in delivery(None)


def test_pickup():
    assert 'Забрали за' in pickup(None)
