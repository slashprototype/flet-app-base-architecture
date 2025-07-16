# 🛍️ Expendio Monitor - Aplicación Reactiva de Ventas

Una aplicación desktop desarrollada en Python usando Flet que simula ventas automáticas y muestra estadísticas en tiempo real. Implementa una arquitectura modular con separación clara de responsabilidades, sistema de eventos pub/sub y preservación del estado de las vistas.

---

## 🚀 Características

* **Simulación automática de ventas** cada X segundos configurable
* **Monitor en tiempo real** con historial de ventas recientes
* **Dashboard de estadísticas** con balance total y promedios
* **Arquitectura modular desacoplada** con separación core/gui/infrastructure
* **Preservación del estado** de las vistas (dropdowns, scroll, inputs)
* **Sistema de logging configurable** por entorno con rotación de archivos
* **Sistema de eventos pub/sub** para comunicación entre componentes
* **Navegación lateral** con cambio de vistas sin pérdida de estado

---

## 🧱 Estructura del Proyecto

```
personal-expendio-2/
├── README.md
├── requirements.txt
├── logs/
│   └── expendio.log         # Logs de la aplicación
├── src/
│   ├── main.py              # Punto de entrada principal
│   ├── core/                # Lógica de negocio central
│   │   ├── __init__.py
│   │   ├── config.py        # Configuración legacy (migrado a infrastructure)
│   │   ├── data_store.py    # Almacén de datos de ventas
│   │   ├── logger.py        # Logger legacy (migrado a infrastructure)
│   │   └── updater.py       # Simulador de ventas automáticas
│   ├── events/              # Sistema de eventos
│   │   ├── __init__.py
│   │   └── dispatcher.py    # Dispatcher pub/sub para eventos
│   ├── gui/                 # Interfaz de usuario
│   │   ├── __init__.py
│   │   ├── bindings.py      # Vinculación datos-UI y sincronización
│   │   ├── views.py         # Importaciones de vistas
│   │   ├── components/      # Componentes reutilizables
│   │   │   ├── __init__.py
│   │   │   └── app_bar.py   # Barra de aplicación superior
│   │   └── views/           # Vistas principales
│   │       ├── __init__.py
│   │       ├── balance_view.py  # Vista de resumen/estadísticas
│   │       └── sales_view.py    # Vista de monitor de ventas
│   ├── infrastructure/      # Infraestructura y servicios
│   │   ├── __init__.py
│   │   ├── config.py        # Sistema de configuración centralizado
│   │   └── logger.py        # Sistema de logging avanzado
│   └── storage/             # Almacenamiento
│       ├── data/            # Datos persistentes
│       └── temp/            # Archivos temporales
```

---

## ⚙️ Configuración

La aplicación utiliza variables de entorno para su configuración. Todas son opcionales y tienen valores por defecto.

### Variables de Logging
```bash
EXPENDIO_LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR, CRITICAL
EXPENDIO_LOG_TO_FILE=true            # true/false - guardar logs en archivo
EXPENDIO_LOG_TO_CONSOLE=true         # true/false - mostrar logs en consola
EXPENDIO_LOG_FILE=logs/expendio.log  # Ruta del archivo de log
EXPENDIO_LOG_MAX_BYTES=10485760      # Tamaño máximo del archivo (10MB)
EXPENDIO_LOG_BACKUP_COUNT=5          # Número de archivos de backup
```

### Variables de Aplicación
```bash
EXPENDIO_MAX_HISTORY=10              # Máximo de ventas en historial
EXPENDIO_SIM_INTERVAL=5              # Intervalo de simulación en segundos
```

### Variables de Ventana
```bash
EXPENDIO_WINDOW_WIDTH=1000           # Ancho de ventana
EXPENDIO_WINDOW_HEIGHT=700           # Alto de ventana
```

---

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.10 o superior
- pip (incluido con Python)

### Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd personal-expendio-2
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

```bash
# Desde el directorio raíz del proyecto
cd src
python main.py
```

La aplicación abrirá una ventana desktop con:
- **Vista de Ventas**: Monitor en tiempo real con historial y estadísticas
- **Vista de Balance**: Resumen detallado con gráficos y métricas

---

## 🎯 Funcionalidades

### Monitor de Ventas
- Simulación automática de ventas cada 5 segundos (configurable)
- Lista en tiempo real de las últimas ventas
- Estadísticas en vivo: número total de ventas y monto acumulado
- Dropdown para revisar ventas específicas
- Scroll automático al final de la lista

### Dashboard de Balance
- Resumen de ventas totales y montos
- Cálculo de promedios por venta
- Visualización de tendencias
- Estadísticas detalladas

### Características Técnicas
- **Persistencia de estado**: Las vistas mantienen su estado al cambiar entre ellas
- **Logging configurable**: Sistema robusto con rotación automática de archivos
- **Arquitectura reactiva**: Eventos pub/sub para comunicación entre componentes
- **Modularidad**: Separación clara entre lógica de negocio, UI e infraestructura

---

## 🏗️ Arquitectura

### Patrones Implementados

* **Clean Architecture**: Separación en capas (core, gui, infrastructure)
* **Publisher-Subscriber**: Sistema de eventos desacoplado
* **View State Preservation**: Mantenimiento del estado entre navegación
* **Dependency Injection**: Configuración centralizada inyectable
* **Repository Pattern**: Abstracción del almacenamiento de datos

### Flujo de Datos

1. **Updater** (core) genera ventas automáticamente
2. **DataStore** (core) almacena el historial
3. **EventDispatcher** notifica cambios a la UI
4. **Bindings** (gui) actualiza las vistas reactivamente
5. **Views** (gui) reflejan los cambios en tiempo real

---

## � Desarrollo

### Estructura de Módulos

- **`src/core/`**: Lógica de negocio pura, independiente de la UI
- **`src/gui/`**: Interfaz de usuario con Flet, componentes y vistas
- **`src/infrastructure/`**: Servicios transversales (config, logging)
- **`src/events/`**: Sistema de comunicación entre componentes

### Agregar Nueva Funcionalidad

1. **Lógica de negocio**: Añadir en `src/core/`
2. **Vista**: Crear en `src/gui/views/`
3. **Navegación**: Actualizar `main.py` y navigation rail
4. **Eventos**: Usar `EventDispatcher` para comunicación
5. **Configuración**: Añadir variables en `infrastructure/config.py`

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

---

## 👨‍💻 Autor

Desarrollado como proyecto de demostración de arquitecturas modulares en Python + Flet.
