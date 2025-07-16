"""
Punto de entrada principal de la aplicación Flet.
"""

import flet as ft
import asyncio
from core import updater
from infrastructure.config import Config
from infrastructure.logger import logger
from gui.views import SalesView, BalanceView
from gui.components import AppBar
from gui.bindings import bind_multiple_views, initialize_multiple_views

class MainApp(ft.Column):
    """Aplicación principal con AppBar y navegación lateral usando View State Preservation Pattern."""
    
    def __init__(self):
        super().__init__()
        self.selected_index = 0
        
        # Componentes principales
        self.app_bar = AppBar()
        self.sales_view = SalesView()
        self.balance_view = BalanceView()
        
        # Contenedores para cada vista - SIEMPRE en la página
        self.sales_container = ft.Container(
            content=self.sales_view,
            padding=20,
            expand=True,
            visible=True  # Vista inicial visible
        )
        
        self.balance_container = ft.Container(
            content=self.balance_view,
            padding=20,
            expand=True,
            visible=False  # Vista oculta inicialmente
        )
        
        # Stack que contiene todas las vistas superpuestas
        self.views_stack = ft.Stack([
            self.sales_container,
            self.balance_container
        ], expand=True)
        
        self._build_layout()
        
        logger.info("🏗️ MainApp inicializada con AppBar y vistas modulares")
    
    def _build_layout(self):
        """Construye el layout principal."""
        # NavigationRail (sidebar)
        self.nav_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.SHOPPING_CART,
                    selected_icon=ft.Icons.SHOPPING_CART,
                    label="Ventas"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.ACCOUNT_BALANCE_WALLET,
                    selected_icon=ft.Icons.ACCOUNT_BALANCE_WALLET,
                    label="Balance"
                )
            ],
            on_change=self._on_nav_change
        )
        
        # Contenido principal (sidebar + vistas)
        main_content = ft.Row([
            self.nav_rail,
            ft.VerticalDivider(width=1),
            self.views_stack
        ], expand=True)
        
        # Layout completo: AppBar + Contenido
        self.controls = [
            self.app_bar,
            main_content
        ]
        self.spacing = 0
        self.expand = True
    
    def _on_nav_change(self, e):
        """Maneja el cambio de navegación usando visibilidad."""
        old_index = self.selected_index
        self.selected_index = e.control.selected_index
        
        view_names = ["Ventas", "Balance"]
        logger.log_navigation(view_names[old_index], view_names[self.selected_index])
        
        self._update_visibility()
        self.update()
    
    def _update_visibility(self):
        """Actualiza la visibilidad de las vistas sin removerlas de la página."""
        if self.selected_index == 0:
            # Mostrar ventas, ocultar balance
            self.sales_container.visible = True
            self.balance_container.visible = False
        else:
            # Mostrar balance, ocultar ventas
            self.sales_container.visible = False
            self.balance_container.visible = True
    
    def setup_bindings_and_initialize(self):
        """Configura eventos e inicializa datos DESPUÉS de estar en la página."""
        logger.info("🔧 Configurando bindings para View State Preservation Pattern")
        
        # Vincular todas las vistas (incluyendo AppBar) a los eventos
        bind_multiple_views(self.sales_view, self.balance_view, self.app_bar)
        
        # Inicializar con datos actuales
        initialize_multiple_views(self.sales_view, self.balance_view, self.app_bar)
        
        # Activar estado en AppBar
        self.app_bar.update_status(True)

async def main(page: ft.Page):
    """Función principal de la aplicación."""
    
    # Configurar logging al inicio
    logger.info("🚀 Iniciando aplicación Expendio Personal")
    
    if Config.LOG_LEVEL == "DEBUG":
        Config.print_config()
    
    # Configuración de la página
    page.title = "🛍️ Monitor de Ventas - Expendio Personal"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_width = Config.WINDOW_WIDTH
    page.window_height = Config.WINDOW_HEIGHT
    page.window_resizable = True # type: ignore
    
    logger.debug(f"Ventana configurada: {Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}")
    
    # Crear la aplicación principal
    main_app = MainApp()
    
    # Agregar la aplicación a la página PRIMERO
    # Esto asegura que TODAS las vistas tengan referencia a page
    page.add(main_app)
    
    # AHORA configurar eventos e inicializar (después de estar en la página)
    main_app.setup_bindings_and_initialize()
    
    logger.info("✅ Aplicación completamente inicializada")
    
    # Lanzar el simulador de ventas en paralelo
    # Esto no bloquea la interfaz de usuario
    asyncio.create_task(updater.start_simulation())

if __name__ == "__main__":
    # Ejecutar la aplicación
    ft.app(target=main)
