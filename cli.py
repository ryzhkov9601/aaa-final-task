import click
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument('pizza_name')
@click.option(
    '--delivery', is_flag=True, default=False,
    help='Доставка заказанной пиццы.')
def order(pizza_name: str, delivery: bool) -> None:
    """Заказать пиццу PIZZA_NAME с опциональной доставкой."""

    if pizza_name.title() not in Pizza.get_pizza_names():
        click.echo('К сожалению, у нас нет этого блюда. Посмотрите наше меню.')
        return
    click.echo('🧑‍🍳 Приготовили за 2 с.')
    if delivery:
        click.echo('🛵 Доставили за 1 с.')


@cli.command()
def menu() -> None:
    """Показать меню."""

    pizzas = [Margherita(), Pepperoni(), Hawaiian()]
    for pizza in pizzas:
        click.echo(pizza)


if __name__ == '__main__':
    cli()
