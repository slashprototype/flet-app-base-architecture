"""
Sistema de configuración centralizado.
Maneja configuraciones a través de variables de entorno.
"""

import os
from enum import Enum

class LogLevel(Enum):
    """Niveles de logging disponibles."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class Config:
    """Configuración centralizada de la aplicación."""
    
    # Configuración de logging
    LOG_LEVEL = os.getenv("EXPENDIO_LOG_LEVEL", "INFO").upper()
    LOG_TO_FILE = os.getenv("EXPENDIO_LOG_TO_FILE", "true").lower() == "true"
    LOG_TO_CONSOLE = os.getenv("EXPENDIO_LOG_TO_CONSOLE", "true").lower() == "true"
    LOG_FILE_PATH = os.getenv("EXPENDIO_LOG_FILE", "logs/expendio.log")
    LOG_MAX_BYTES = int(os.getenv("EXPENDIO_LOG_MAX_BYTES", "10485760"))  # 10MB
    LOG_BACKUP_COUNT = int(os.getenv("EXPENDIO_LOG_BACKUP_COUNT", "5"))
    
    # Configuración de la aplicación
    MAX_SALES_HISTORY = int(os.getenv("EXPENDIO_MAX_HISTORY", "10"))
    SIMULATION_INTERVAL = int(os.getenv("EXPENDIO_SIM_INTERVAL", "5"))
    
    # Configuración de la ventana
    WINDOW_WIDTH = int(os.getenv("EXPENDIO_WINDOW_WIDTH", "1000"))
    WINDOW_HEIGHT = int(os.getenv("EXPENDIO_WINDOW_HEIGHT", "700"))
    
    @classmethod
    def get_log_level(cls):
        """Obtiene el nivel de logging configurado."""
        try:
            return getattr(LogLevel, cls.LOG_LEVEL)
        except AttributeError:
            return LogLevel.INFO
    
    @classmethod
    def print_config(cls):
        """Imprime la configuración actual para debugging."""
        print("🔧 Configuración de Expendio:")
        print(f"  Log Level: {cls.LOG_LEVEL}")
        print(f"  Log to File: {cls.LOG_TO_FILE}")
        print(f"  Log to Console: {cls.LOG_TO_CONSOLE}")
        print(f"  Max History: {cls.MAX_SALES_HISTORY}")
        print(f"  Simulation Interval: {cls.SIMULATION_INTERVAL}s")
