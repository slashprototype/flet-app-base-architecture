# 🛍️ Expendio Monitor - Aplicación Reactiva de Ventas

Una aplicación Flet en Python que simula ventas automáticas y muestra estadísticas en tiempo real. Ideal para proyectos que requieren interfaces reactivas, modularidad y separación de lógica de UI.

---

## 🚀 Características

* Simulación de ventas automáticas cada X segundos
* Visualización de historial reciente de ventas
* Estadísticas de balance total y promedio
* Arquitectura modular desacoplada
* Persistencia del estado de las vistas (dropdowns, scroll, inputs)
* Sistema de logging centralizado por entorno

---

## 🧱 Estructura del Proyecto

```
├── core/
│   ├── config.py            # Configuración centralizada
│   ├── logger.py            # Sistema de logging
│   ├── data_store.py        # Historial de ventas
│   └── updater.py           # Simulador de ventas periódicas
│
├── events/
│   └── dispatcher.py        # Sistema pub/sub para eventos internos
│
├── gui/
│   ├── components/
│   │   └── app_bar.py       # Componentes compartidos
│   ├── views/
│   │   ├── sales_view.py    # Vista de ventas
│   │   └── balance_view.py  # Vista de resumen de ventas
│   └── bindings.py          # Sincronización de datos con UI
│
└── main.py                  # Entrypoint con gestión de navegación
```

---

## ⚙️ Configuración (Variables de entorno)

```bash
# Logging
export EXPENDIO_LOG_LEVEL=DEBUG          # DEBUG, INFO, WARNING, ERROR, CRITICAL
export EXPENDIO_LOG_TO_FILE=true         # true/false
export EXPENDIO_LOG_TO_CONSOLE=true      # true/false
export EXPENDIO_LOG_FILE=logs/app.log    # Ruta del archivo de log

# Aplicación
export EXPENDIO_MAX_HISTORY=15           # Máximo de ventas en historial
export EXPENDIO_SIM_INTERVAL=3           # Intervalo de simulación en segundos

# Ventana
export EXPENDIO_WINDOW_WIDTH=1200        # Ancho de ventana
export EXPENDIO_WINDOW_HEIGHT=800        # Alto de ventana
```

---

## ▶️ Cómo ejecutar

```bash
# Crear entorno virtual
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows

# Instalar dependencias
pip install flet python-dotenv

# Ejecutar la aplicación
python main.py
```

---

## 📊 Captura de pantalla (opcional)

Agrega aquí una imagen de ejemplo de la interfaz.

---

## 🧩 Patrón de diseño usado

* **Arquitectura Modular por Dominio**
* **Patrón Reactivo (event-driven + pub/sub)**
* **Preservación de estado visual** mediante `Stack + visibility`
* **Inyección de configuración por entorno**
* **Logging desacoplado y centralizado**

---

## 🧑‍💻 Créditos

Desarrollado por Slashprotoype. Basado en Flet + Python 3.10+.

---

## 📝 Licencia

Este proyecto está licenciado bajo los términos de la MIT License.
