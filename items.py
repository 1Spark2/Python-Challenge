import pandas as pd
from rich.table import Table
from rich.console import Console


# Clase para manipular los datos usando pandas
class ProductInventory:
    def __init__(self):
        self._products_df = pd.DataFrame({
            "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
            "quantity": [3, 10, 0, 5],
            "price": [1.50, 2.00, 1.75, 2.50]
        })
    

    # Listar los productos en una tabla
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