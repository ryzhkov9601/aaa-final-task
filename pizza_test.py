import pytest
from pizza import Pizza, Size, EmojiMixin


class TestPizza:
    @pytest.fixture
    def simple_pizza(self):
        """Объект класса Pizza для тестов."""

        return Pizza('test', ['first', 'second'])

    def test_str(self, simple_pizza):
        assert str(simple_pizza) == "- test: first, second"

    def test_size_setter(self, simple_pizza):
        with pytest.raises(ValueError):
            simple_pizza.size = 'L'

    def test_dict_keys(self, simple_pizza):
        assert simple_pizza.dict().keys() == {'name', 'recipe', 'size'}

    def test_dict(self, simple_pizza):
        expected = {
            'name': 'test',
            'recipe': ['first', 'second'],
            'size': Size.L
        }
        assert simple_pizza.dict() == expected

    def test_eq(self, simple_pizza):
        assert simple_pizza == Pizza('test', ['first', 'second'])

    def test_ne(self, simple_pizza):
        assert simple_pizza != Pizza('test', ['first', 'second'], Size.XL)


class TestEmojiMixin:
    @pytest.fixture
    def simple_class(self):
        """Простой класс с атрибутами name, emoji и методом __str__."""

        class A(EmojiMixin):
            emoji = '🧪'
            name = 'testing'

            def __str__(self) -> str:
                return self.name
        return A

    def test_str(self, simple_class):
        assert str(simple_class()) == 'testing🧪'

    def test_name(self, simple_class):
        a = simple_class()
        str(a)
        assert a.name == 'testing'
