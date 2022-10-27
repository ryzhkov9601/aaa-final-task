import pytest

from click.testing import CliRunner
from cli import cli


@pytest.fixture
def cli_result(request):
    """Результат выполнения команды в группе cli."""

    return CliRunner().invoke(cli, request.param)


@pytest.fixture
def order_result(request):
    """Результат выполнения команды order."""

    return CliRunner().invoke(cli, ['order', request.param])


@pytest.fixture
def order_result_with_delivery(request):
    """Результат выполнения команды order с флагом delivery."""

    return CliRunner().invoke(cli, ['order', '--delivery', request.param])


@pytest.mark.parametrize(
    'order_result',
    ['pepperoni', 'margherita', 'hawaiian'],
    indirect=True
    )
def test_order(order_result):
    assert order_result.exit_code == 0
    assert '🧑‍🍳 Приготовили' in order_result.output
    assert '🏠 Забрали' in order_result.output
    assert '🛵 Доставили' not in order_result.output


@pytest.mark.parametrize(
    'order_result_with_delivery',
    ['pepperoni', 'margherita', 'hawaiian'],
    indirect=True
    )
def test_order_with_delivery(order_result_with_delivery):
    assert order_result_with_delivery.exit_code == 0
    assert '🧑‍🍳 Приготовили' in order_result_with_delivery.output
    assert '🛵 Доставили' in order_result_with_delivery.output
    assert '🏠 Забрали' not in order_result_with_delivery.output


@pytest.mark.parametrize(
    'order_result',
    ['hamburger', 'ice-cream'],
    indirect=True
    )
def test_wrong_order(order_result):
    expected = 'К сожалению, у нас нет этого блюда. Посмотрите наше меню.'
    assert order_result.exit_code == 0
    assert expected in order_result.output


@pytest.mark.parametrize(
    'cli_result',
    ['menu'],
    indirect=True
    )
def test_menu(cli_result):
    assert cli_result.exit_code == 0
    assert 'Margherita' in cli_result.output
    assert 'Pepperoni' in cli_result.output
    assert 'Hawaiian' in cli_result.output
