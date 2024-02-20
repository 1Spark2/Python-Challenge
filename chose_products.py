from items import ProductInventory  # Asegúrate de que esta es la ubicación correcta de tu clase ProductInventory
import typer
from rich import print as rprint


class ShopInterface:
    def __init__(self):
        self.inventory = ProductInventory()


    def choose_product(self):
        while True:
            self.inventory.list_products()
            selection = typer.prompt("Por favor, ingresa el id del producto que deseas")
            try:
                index = int(selection) - 1
                if index >= 0 and index < len(self.inventory._products_df):
                    product_info = self.inventory._products_df.iloc[index]
                    if product_info['quantity'] > 0:
                        return product_info.to_dict()  # Convertir a diccionario aquí
                    else:
                        rprint(f"\nDisculpa, pero no tenemos stock de [bold]{product_info['product_name']}[/bold]. Por favor elige otro.")
                        self.inventory._products_df.drop(index, inplace=True)
                        self.inventory._products_df.reset_index(drop=True, inplace=True)
                else:
                    typer.echo("Selección inválida. Por favor, intenta de nuevo.")
            except ValueError:
                typer.echo("Por favor, ingresa un número válido.")

    
    def apply_discount(self, product_info):
        discount_code = "DESC15"
        attempts = 0
        full_price = product_info['price']  # Precio completo por defecto
        discounted_price = full_price  # Inicializa con el precio completo en caso de que no se aplique el descuento
    
        while attempts < 3:
            user_code = typer.prompt("\nOye, tenemos este código de descuento DESC15.\nIngresa este código al momento de realizar la compra para obtener 15% de descuento.\nIngresa el codigo:")
            if user_code == discount_code:
                discount_amount = full_price * 0.15  # Calcula el monto del descuento
                discounted_price = full_price - discount_amount
                rprint(f"\n¡Código de descuento válido! Has ahorrado: [bold green]${discount_amount:.2f}[/bold green]")
                break
            else:
                rprint("\n[bold]Código de descuento inválido[/bold].")
                attempts += 1
                if attempts < 3:
                    typer.echo("\nIntenta nuevamente.")
                else:
                    typer.echo("\nSe han superado los intentos permitidos. El código no podrá ser aplicado.")
    
        return discounted_price  # Retorna el precio final después del intento de aplicar el descuento

