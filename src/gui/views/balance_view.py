"""
Vista de balance total de ventas.
"""

import flet as ft
from infrastructure.logger import logger

class BalanceView(ft.Column):
    """Vista que muestra el balance total de ventas."""
    
    def __init__(self):
        super().__init__()
        self.total_amount = 0.0
        self.total_sales = 0
        self.balance_text = None
        self.sales_count_text = None
        self.average_text = None
        self.spacing = 20
        self._build_components()
        
        logger.debug("🏗️ BalanceView inicializada")
    
    def _build_components(self):
        """Construye los componentes de la vista de balance."""
        # Título
        title = ft.Text(
            "💰 Balance Total",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_700
        )
        
        # Balance principal
        self.balance_text = ft.Text(
            f"${self.total_amount:.2f}",
            size=48,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_600
        )
        
        # Número de ventas
        self.sales_count_text = ft.Text(
            f"Total de ventas: {self.total_sales}",
            size=18,
            color=ft.Colors.BLUE_700
        )
        
        # Promedio por venta
        self.average_text = ft.Text(
            f"Promedio por venta: $0.00",
            size=16,
            color=ft.Colors.GREY_700
        )
        
        # Contenedor principal con estilo
        balance_container = ft.Container(
            content=ft.Column([
                self.balance_text,
                self.sales_count_text,
                self.average_text
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            padding=40,
            border_radius=15,
            bgcolor=ft.Colors.LIGHT_BLUE_100,
            border=ft.border.all(2, ft.Colors.GREEN_200),
            width=400,
            alignment=ft.alignment.center
        )
        
        # Icono decorativo
        icon = ft.Icon(
            ft.Icons.ACCOUNT_BALANCE_WALLET,
            size=64,
            color=ft.Colors.GREEN_600
        )
        
        # Agregar controles a la columna principal
        self.controls = [
            title,
            ft.Divider(height=20),
            icon,
            ft.Divider(height=20),
            balance_container,
            ft.Divider(height=20),
            ft.Text(
                "💡 Este balance se actualiza automáticamente con cada nueva venta",
                size=12,
                italic=True,
                color=ft.Colors.BLUE_600
            )
        ]
        
        # Centrar todo
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def update_sales(self, sales):
        """Actualiza el balance basado en las ventas."""
        # Verificar que el control esté en la página antes de actualizar
        if not self.balance_text or not hasattr(self, 'page') or self.page is None:
            return
            
        # Calcula totales
        self.total_sales = len(sales)
        self.total_amount = sum(sale.get('precio', 0) for sale in sales)
        average = self.total_amount / self.total_sales if self.total_sales > 0 else 0
        
        # Actualiza textos
        self.balance_text.value = f"${self.total_amount:.2f}"
        self.sales_count_text.value = f"Total de ventas: {self.total_sales}"
        self.average_text.value = f"Promedio por venta: ${average:.2f}"
        
        logger.log_ui_update("BalanceView", len(sales))
        self.update()
