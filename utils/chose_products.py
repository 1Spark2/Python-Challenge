from utils.items import ProductInventory
import typer
from rich import print as rprint
from typing import Dict, Optional

class ShopInterface:
    def __init__(self):
        self.inventory = ProductInventory()

    # Escoge el producto, si el producto elegido tiene la cantidad de 0 unidades-
    # -de stock lo elimina de la tabla.
    def choose_product(self) -> Optional[Dict[str, any]]:
        while True:
            self.inventory.list_products()
            selection = typer.prompt("\nPor favor, ingresa el id del producto que deseas")
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
                    typer.echo("\nSelección inválida. Por favor, intenta de nuevo.\n")
            except ValueError:
                typer.echo("Por favor, ingresa un número válido.")

    
    # Provee a el usuario de un cupon de descuento al usuario y de no ser usado efectivamente realiza-
    # -la operacion sin este.
    def apply_discount(self, product_info: Dict[str, any]) -> float:
        discount_code = "DESC15"
        attempts = 0
        discount_applied = False
        while attempts < 3:
            user_code = typer.prompt("\nOye, tenemos este código de descuento DESC15.\nIngresa este código al momento de realizar la compra para obtener 15% de descuento.\nIngresa el codigo").upper()
            if user_code == discount_code:
                discount_amount = product_info['price'] * 0.15  # 15% de descuento.
                final_price = product_info['price'] - discount_amount
                rprint(f"\n¡Código de descuento válido! Tu descuento es: [bold green]${discount_amount:.2f}[/bold green]")
                discount_applied = True
                break
            else:
                rprint("\n[bold]Código de descuento inválido[/bold].")
                attempts += 1
                if attempts == 3:
                    rprint("\nSe han superado los intentos permitidos. El código no podrá ser aplicado.")

        if not discount_applied:
            final_price = product_info['price']

        return final_price

    # Mostrar detalles del pedido, precio final y confirmacion de la compra
    def confirm_order(self, product_info, final_price):
        rprint(f"\nTu pedido de helado de [bold]{product_info['product_name']}[/bold] con un precio de [bold green]${final_price:.2f}[/bold green] está casi listo.")
        if typer.confirm("¿Quieres confirmar la compra?"):
            rprint("\nTu pedido ha sido confirmado:D. Disfruta el sabroso helado de Heladerías Frozen SRL. Esperamos volver a verte pronto!\n")
        else:
            rprint("\nPedido cancelado:C. Esperamos que vuelvas pronto para disfrutar de nuestro delicioso helado.\n")


