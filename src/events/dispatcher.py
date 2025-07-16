"""
Manejador de eventos simple (pub/sub).
"""

from infrastructure.logger import logger

subscribers = {}

def subscribe(event, callback):
    """Suscribe un callback a un evento específico."""
    if event not in subscribers:
        subscribers[event] = []
    subscribers[event].append(callback)
    logger.debug(f"📡 Nuevo suscriptor para evento '{event}'. Total: {len(subscribers[event])}")

def dispatch(event, data=None):
    """Emite un evento a todos los suscriptores."""
    callback_count = len(subscribers.get(event, []))
    logger.debug(f"📢 Despachando evento '{event}' a {callback_count} suscriptores")
    
    for callback in subscribers.get(event, []):
        try:
            callback(data)
        except Exception as e:
            logger.error(f"💥 Error en callback del evento {event}: {e}")

def unsubscribe(event, callback):
    """Desuscribe un callback de un evento."""
    if event in subscribers and callback in subscribers[event]:
        subscribers[event].remove(callback)
        logger.debug(f"🔇 Suscriptor removido del evento '{event}'")
