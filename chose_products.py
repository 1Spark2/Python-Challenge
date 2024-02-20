from products import ProductInventory  # Asegúrate de que esta es la ubicación correcta de tu clase ProductInventory
import typer


class ShopInterface:
    def __init__(self):
        self.inventory = ProductInventory()


    def choose_product(self):
        while True:
            self.inventory.list_products()
            selection = typer.prompt("Por favor, ingresa el número del producto que deseas")
            try:
                index = int(selection) - 1
                if index >= 0 and index < len(self.inventory._products_df):
                    product_info = self.inventory._products_df.iloc[index]
                    if product_info['quantity'] > 0:
                        return product_info.to_dict()  # Convertir a diccionario aquí
                    else:
                        typer.echo(f"Disculpa, pero no tenemos stock de {product_info['product_name']}. Por favor elige otro.")
                        self.inventory._products_df.drop(index, inplace=True)
                        self.inventory._products_df.reset_index(drop=True, inplace=True)
                else:
                    typer.echo("Selección inválida. Por favor, intenta de nuevo.")
            except ValueError:
                typer.echo("Por favor, ingresa un número válido.")

    
    def apply_discount(self, product_info):
        discount_code = "DESC15"
        attempts = 0
        while attempts < 3:
            user_code = typer.prompt("Oye, tenemos este código de descuento DESC15. Ingresa este código al momento de realizar la compra para obtener 15% de descuento.\nIngresa el codigo")
            if user_code == discount_code:
                discounted_price = product_info['price'] * 0.85
                typer.echo(f"¡Código de descuento válido! El nuevo precio con descuento es: ${discounted_price:.2f}")
                break
            else:
                typer.echo("Código de descuento inválido.")
                attempts += 1
                if attempts < 3:
                    typer.echo("Intenta nuevamente.")
                else:
                    typer.echo("Se han superado los intentos permitidos. El codigo no podra ser aplicado.")

