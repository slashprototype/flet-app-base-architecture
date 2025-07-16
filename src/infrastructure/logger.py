"""
Sistema de logging centralizado y configurable.
"""

import logging
import logging.handlers
import os
from datetime import datetime
from infrastructure.config import Config

class AppLogger:
    """Logger centralizado de la aplicación."""
    
    _instance = None
    _logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._setup_logger()
        return cls._instance
    
    def _setup_logger(self):
        """Configura el sistema de logging."""
        self._logger = logging.getLogger("expendio")
        self._logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        
        # Limpiar handlers existentes
        self._logger.handlers.clear()
        
        # Formato de logs
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Handler para consola
        if Config.LOG_TO_CONSOLE:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self._logger.addHandler(console_handler)
        
        # Handler para archivo
        if Config.LOG_TO_FILE:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(Config.LOG_FILE_PATH), exist_ok=True)
            
            file_handler = logging.handlers.RotatingFileHandler(
                Config.LOG_FILE_PATH,
                maxBytes=Config.LOG_MAX_BYTES,
                backupCount=Config.LOG_BACKUP_COUNT,
                encoding='utf-8'
            )
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)
        
        # Log inicial
        self._logger.info("🚀 Sistema de logging iniciado")
        self._logger.debug(f"Configuración: Level={Config.LOG_LEVEL}, File={Config.LOG_TO_FILE}, Console={Config.LOG_TO_CONSOLE}")
    
    def debug(self, message):
        """Log nivel DEBUG."""
        self._logger.debug(message)
    
    def info(self, message):
        """Log nivel INFO."""
        self._logger.info(message)
    
    def warning(self, message):
        """Log nivel WARNING."""
        self._logger.warning(message)
    
    def error(self, message):
        """Log nivel ERROR."""
        self._logger.error(message)
    
    def critical(self, message):
        """Log nivel CRITICAL."""
        self._logger.critical(message)
    
    def log_sale(self, sale):
        """Log específico para ventas."""
        self._logger.info(f"💰 Nueva venta: {sale['producto']} - ${sale['precio']:.2f} @ {sale['hora']}")
    
    def log_ui_update(self, view_name, data_count):
        """Log específico para actualizaciones de UI."""
        self._logger.debug(f"🔄 UI actualizada: {view_name} con {data_count} elementos")
    
    def log_navigation(self, from_view, to_view):
        """Log específico para navegación."""
        self._logger.debug(f"🧭 Navegación: {from_view} → {to_view}")

# Instancia global del logger
logger = AppLogger()
