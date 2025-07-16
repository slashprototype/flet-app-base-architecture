"""
Barra de aplicación superior con estado y contadores.
"""

import flet as ft
from infrastructure.logger import logger

class AppBar(ft.Container):
    """Barra de aplicación con status y contadores."""
    
    def __init__(self):
        super().__init__()
        self.total_sales = 0
        self.total_amount = 0.0
        self.status_icon = None
        self.sales_counter = None
        self.balance_text = None
        self._build_components()
        
        logger.debug("🏗️ AppBar inicializada")
    
    def _build_components(self):
        """Construye los componentes de la barra de aplicación."""
        # Icono de estado
        self.status_icon = ft.Icon(
            ft.Icons.CIRCLE,
            color=ft.Colors.GREEN,
            size=16
        )
        
        # Contador de ventas
        self.sales_counter = ft.Text(
            f"📊 {self.total_sales} ventas",
            size=14,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD
        )
        
        # Balance total
        self.balance_text = ft.Text(
            f"💰 ${self.total_amount:.2f}",
            size=14,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD
        )
        
        # Título de la aplicación
        title = ft.Text(
            "🛍️ Expendio Personal",
            size=18,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD
        )
        
        # Contenedor principal
        self.content = ft.Row([
            ft.Row([
                self.status_icon,
                title
            ], spacing=10),
            ft.Row([
                self.sales_counter,
                ft.VerticalDivider(width=1, color=ft.Colors.WHITE30),
                self.balance_text
            ], spacing=15)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        
        self.bgcolor = ft.Colors.BLUE_700
        self.padding = ft.padding.symmetric(horizontal=20, vertical=15)
        self.border_radius = 0
    
    def update_status(self, is_active: bool):
        """Actualiza el estado de la aplicación."""
        if not hasattr(self, 'page') or self.page is None:
            return
            
        self.status_icon.color = ft.Colors.GREEN if is_active else ft.Colors.RED
        logger.debug(f"🔄 Estado actualizado: {'Activo' if is_active else 'Inactivo'}")
        self.update()
    
    def update_counters(self, sales_count: int, total_amount: float):
        """Actualiza los contadores de ventas y balance."""
        if not hasattr(self, 'page') or self.page is None:
            return
            
        self.total_sales = sales_count
        self.total_amount = total_amount
        
        self.sales_counter.value = f"📊 {self.total_sales} ventas"
        self.balance_text.value = f"💰 ${self.total_amount:.2f}"
        
        logger.log_ui_update("AppBar", sales_count)
        self.update()
