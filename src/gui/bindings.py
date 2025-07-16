"""
Enlaza el data_store con la interfaz de usuario mediante eventos.
"""

from events import dispatcher
from core import data_store
from core.logger import logger

bindings = []

def bind_sales_to_view(view):
    """Vincula las ventas del data store con la vista."""
    
    def on_new_sale(sale_data):
        """Callback que se ejecuta cuando hay una nueva venta."""
        # Verificar que la vista esté en la página antes de actualizar
        if not hasattr(view, 'page') or view.page is None:
            return
            
        current_sales = data_store.get_sales()
        
        # Diferentes tipos de vista requieren diferentes actualizaciones
        if hasattr(view, 'update_sales'):
            # Vista normal (SalesView, BalanceView)
            view.update_sales(current_sales)
        elif hasattr(view, 'update_counters'):
            # AppBar
            total_amount = sum(sale.get('precio', 0) for sale in current_sales)
            view.update_counters(len(current_sales), total_amount)
    
    # Suscribe el callback al evento
    dispatcher.subscribe("SALE_ADDED", on_new_sale)
    bindings.append(view)  # Opcional para limpieza posterior
    
    # Store the callback for later initialization
    view._on_new_sale = on_new_sale

def bind_multiple_views(*views):
    """Vincula múltiples vistas a los eventos de ventas."""
    for view in views:
        bind_sales_to_view(view)

def initialize_view_data(view):
    """Inicializa la vista con datos actuales después de que esté en la página."""
    # Solo inicializar si la vista ya está en la página
    if hasattr(view, '_on_new_sale') and hasattr(view, 'page') and view.page is not None:
        view._on_new_sale(None)

def initialize_multiple_views(*views):
    """Inicializa múltiples vistas con datos actuales."""
    for view in views:
        initialize_view_data(view)

def cleanup_bindings():
    """Limpia todas las vinculaciones (útil para cleanup)."""
    global bindings
    bindings = []
