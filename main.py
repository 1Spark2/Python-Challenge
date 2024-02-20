import typer
from geo_api import GeoAPI
from chose_products import ShopInterface  # Asegúrate de que este importe sea correcto

app = typer.Typer()

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
        additional_message = "En Pehuajó la temperatura está más de 28 grados Celsius. ¿Comerás helado para refrescarte?"
    else:
        additional_message = "En Pehuajó la temperatura está a menos de 28 grados Celsius. ¡Un buen día para disfrutar de nuestros helados igualmente!"
    draw_rectangle_around_text(additional_message, 2)

    response = typer.confirm("¿Te gustaría un helado para refrescarte?")
    if response:
        shop_interface = ShopInterface()
        product_info = shop_interface.choose_product()
        if product_info:
            typer.echo(f"Has seleccionado {product_info['product_name']}.")
            shop_interface.apply_discount(product_info)
    else:
        typer.echo("¡Entendido! Esperamos verte en un día más caluroso.")

if __name__ == "__main__":
    app()
