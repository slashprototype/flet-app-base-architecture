"""
Vista de monitor de ventas en tiempo real.
"""

import flet as ft
from infrastructure.logger import logger

class SalesView(ft.Column):
    """Vista principal que muestra las ventas."""
    
    def __init__(self):
        super().__init__()
        self.sales_column = None
        self.sales_dropdown = None
        self.total_sales = 0
        self.total_amount = 0.0
        self.stats_text = None
        self.spacing = 10
        self._build_components()
        
        logger.debug("🏗️ SalesView inicializada")
    
    def _build_components(self):
        """Construye los componentes de la interfaz de usuario."""
        # Título
        title = ft.Text(
            "🛍️ Monitor de Ventas en Tiempo Real",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_700
        )
        
        # Estadísticas
        self.stats_text = ft.Text(
            f"📊 Ventas: {self.total_sales} | 💰 Total: ${self.total_amount:.2f}",
            size=16,
            color=ft.Colors.GREEN_700
        )
        
        # Dropdown para seleccionar ventas
        self.sales_dropdown = ft.Dropdown(
            label="🔍 Seleccionar venta",
            hint_text="Selecciona una venta de la lista",
            width=400,
            options=[]
        )
        
        # Columna de ventas
        self.sales_column = ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            height=350,
            spacing=5
        )
        
        # Contenedor de ventas
        sales_container = ft.Container(
            content=self.sales_column,
            border=ft.border.all(1, ft.Colors.GREY_400),
            border_radius=10,
            padding=10,
            bgcolor=ft.Colors.GREY_50
        )
        
        # Agregar controles a la columna principal
        self.controls = [
            title,
            self.stats_text,
            ft.Divider(height=20),
            self.sales_dropdown,
            ft.Divider(height=10),
            ft.Text("📋 Últimas ventas:", size=18, weight=ft.FontWeight.BOLD),
            sales_container
        ]
    
    def update_sales(self, sales):
        """Actualiza la lista de ventas en la UI."""
        # Verificar que el control esté en la página antes de actualizar
        if not self.sales_column or not hasattr(self, 'page') or self.page is None:
            return
            
        # Calcula estadísticas
        self.total_sales = len(sales)
        self.total_amount = sum(sale.get('precio', 0) for sale in sales)
        
        # Actualiza estadísticas
        self.stats_text.value = f"📊 Ventas: {self.total_sales} | 💰 Total: ${self.total_amount:.2f}"
        
        # Actualiza dropdown options
        self.sales_dropdown.options = []
        for i, sale in enumerate(sales):
            option_text = f"#{i+1} - {sale['producto']} - ${sale['precio']:.2f} ({sale['hora']})"
            self.sales_dropdown.options.append(
                ft.dropdown.Option(key=str(i), text=option_text)
            )
        
        # Si no hay ventas, añadir opción vacía
        if not sales:
            self.sales_dropdown.options = [
                ft.dropdown.Option(key="empty", text="No hay ventas disponibles")
            ]
        
        # Actualiza lista de ventas
        self.sales_column.controls = []
        for i, sale in enumerate(sales):
            sale_card = ft.Container(
                content=ft.Row([
                    ft.Text(f"#{i+1}", size=12, color=ft.Colors.GREY_600),
                    ft.Text(sale['producto'], size=14, expand=True),
                    ft.Text(f"${sale['precio']:.2f}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(sale['hora'], size=12, color=ft.Colors.GREY_600)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=8,
                border_radius=5,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300)
            )
            self.sales_column.controls.append(sale_card)
        
        # Si no hay ventas
        if not sales:
            self.sales_column.controls.append(
                ft.Text(
                    "No hay ventas aún... Esperando nuevas ventas 🔄",
                    size=14,
                    italic=True,
                    color=ft.Colors.GREY_600
                )
            )
        
        logger.log_ui_update("SalesView", len(sales))
        self.update()
