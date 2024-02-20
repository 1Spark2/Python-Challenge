import typer
from geo_api import GeoAPI
from chose_products import ShopInterface  # Verifica el nombre del módulo y la importación
from rich import print as rprint


app = typer.Typer()
shop_interface = ShopInterface()  # Crea la instancia de ShopInterface fuera de la función

def draw_rectangle_around_text(text: str, padding: int = 1):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border_line = '+' + '-' * (max_length + padding * 2) + '+'

    typer.echo(border_line)
    for line in lines:
        typer.echo('|' + line.center(max_length + padding * 2) + '|')
    typer.echo(border_line)

@app.command()
def welcome():
    temp = GeoAPI.is_hot_in_pehuajo()
    message = "¡Hola! Bienvenido a Heladerías Frozen SRL."
    draw_rectangle_around_text(message, 2)
        
    if temp:
        additional_message = "En Pehuajó la temperatura está a más de 28 grados Celsius.\n¿Comerás helado para refrescarte?"
    else:
        additional_message = "En Pehuajó la temperatura está a menos de 28 grados Celsius.\n¡Un buen día para disfrutar de nuestros helados igualmente!"
    draw_rectangle_around_text(additional_message, 2)

    response = typer.confirm("¿Te gustaría un helado para refrescarte?")
    if response:
        product_info = shop_interface.choose_product()
        if product_info:
            rprint(f"\nHas seleccionado [bold]{product_info['product_name']}[/bold].")
            final_price = shop_interface.apply_discount(product_info)
            shop_interface.confirm_order(product_info, final_price)
    else:
        typer.echo("¡Entendido! Esperamos verte en un día más caluroso.")

if __name__ == "__main__":
    app()
