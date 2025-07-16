"""
Interfaz de usuario principal usando Flet.
"""

import flet as ft

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
            height=350,  # Reduced to make room for dropdown
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
        if not self.stats_text:
            self.stats_text = ft.Text()
        self.stats_text.value = f"📊 Ventas: {self.total_sales} | 💰 Total: ${self.total_amount:.2f}"
        
        # Actualiza dropdown options
        if not self.sales_dropdown:
            self.sales_dropdown = ft.Dropdown()
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
        
        self.update()


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
        if not self.balance_text:
            self.balance_text = ft.Text()
        if not self.sales_count_text:
            self.sales_count_text = ft.Text()
        if not self.average_text:
            self.average_text = ft.Text()
        self.balance_text.value = f"${self.total_amount:.2f}"
        self.sales_count_text.value = f"Total de ventas: {self.total_sales}"
        self.average_text.value = f"Promedio por venta: ${average:.2f}"
        
        self.update()
