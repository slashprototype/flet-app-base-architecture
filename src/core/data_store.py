"""
Almacén de datos para las ventas recientes.
Mantiene un historial limitado de ventas.
"""

from infrastructure.config import Config
from infrastructure.logger import logger

sales_history = []

def add_sale(sale):
    """Añade una nueva venta al historial."""
    sales_history.insert(0, sale)
    if len(sales_history) > Config.MAX_SALES_HISTORY:
        removed_sale = sales_history.pop()
        logger.debug(f"🗑️ Venta removida del historial: {removed_sale['producto']}")
    
    logger.debug(f"📝 Venta añadida al almacén. Total: {len(sales_history)}")

def get_sales():
    """Obtiene una copia del historial de ventas."""
    return sales_history.copy()

def clear_sales():
    """Limpia el historial de ventas."""
    global sales_history
    count = len(sales_history)
    sales_history = []
    logger.info(f"🧹 Historial limpiado. {count} ventas removidas")
