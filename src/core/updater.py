"""
Generador de ventas simuladas periódicamente.
"""

import asyncio
import random
from datetime import datetime
from core import data_store
from infrastructure.config import Config
from infrastructure.logger import logger
from events import dispatcher

PRODUCTS = ["🍎 Manzana", "🍞 Pan", "🧃 Jugo", "🥛 Leche", "🥣 Cereal", "🍌 Banana", "🧀 Queso"]

async def start_simulation():
    """Inicia la simulación de ventas cada N segundos según configuración."""
    logger.info(f"🚀 Iniciando simulación con intervalo de {Config.SIMULATION_INTERVAL} segundos")
    
    while True:
        # Genera una venta aleatoria
        sale = {
            "producto": random.choice(PRODUCTS),
            "precio": round(random.uniform(1.50, 15.99), 2),
            "hora": datetime.now().strftime("%H:%M:%S")
        }
        
        # Añade la venta al almacén
        data_store.add_sale(sale)
        
        # Log de la venta
        logger.log_sale(sale)
        
        # Emite el evento
        dispatcher.dispatch("SALE_ADDED", sale)
        
        # Espera según configuración
        await asyncio.sleep(Config.SIMULATION_INTERVAL)
