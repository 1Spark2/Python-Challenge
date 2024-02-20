import pandas as pd

class ProductInventory:
    def __init__(self):
        self._products_df = pd.DataFrame({
            "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
            "quantity": [3, 10, 0, 5],
            "price": [1.50, 2.00, 1.75, 2.50]
        })
    
    def list_products(self):
        """Imprime la lista de productos con índices."""
        print("Productos disponibles:")
        for index, row in self._products_df.iterrows():
            available = 'No disponible' if row['quantity'] <= 0 else f"Cantidad: {row['quantity']}"
            print(f"{index + 1}. {row['product_name']} - {available}, Precio: ${row['price']}")
        print("\nSelecciona el número del producto que deseas comprar.")

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
