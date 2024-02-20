import pandas as pd
from rich.table import Table
from rich.console import Console

class ProductInventory:
    def __init__(self):
        self._products_df = pd.DataFrame({
            "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
            "quantity": [3, 10, 0, 5],
            "price": [1.50, 2.00, 1.75, 2.50]
        })
    
    def list_products(self):
        """Imprime la lista de productos en una tabla."""
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Producto", min_width=20, style="yellow")
        table.add_column("Cantidad", justify="right")
        table.add_column("Precio", justify="right" , style="green")

        for index, row in self._products_df.iterrows():
            available = 'No disponible' if row['quantity'] <= 0 else str(row['quantity'])
            table.add_row(str(index + 1), row['product_name'], available, f"${row['price']}")

        console = Console()
        console.print(table)

    def is_product_available(self, product_name, quantity):
        """Verifica si un producto está disponible en la cantidad solicitada."""
        product = self._products_df[self._products_df['product_name'] == product_name]
        if not product.empty and product.iloc[0]['quantity'] >= quantity:
            return True
        else:
            return False

    def get_product_info(self, product_name):
        """Obtiene la información de un producto específico."""
        product = self._products_df[self._products_df['product_name'] == product_name]
        if not product.empty:
            return product.iloc[0].to_dict()
        else:
            return None

    def remove_unavailable_product(self, product_name):
        """Elimina un producto no disponible de la lista de productos."""
        self._products_df = self._products_df[self._products_df['product_name'] != product_name].reset_index(drop=True)

    def get_product_info_by_index(self, index):
        """Obtiene la información de un producto específico por su índice."""
        if index >= 0 and index < len(self._products_df):
            return self._products_df.iloc[index].to_dict()
        else:
            return None
