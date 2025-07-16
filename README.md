# 🛍️ Expendio Monitor - Aplicación Reactiva de Ventas

Una aplicación desktop desarrollada en Python usando Flet que simula ventas automáticas y muestra estadísticas en tiempo real. Implementa una arquitectura modular con separación clara de responsabilidades, sistema de eventos pub/sub y preservación del estado de las vistas.

---

## 🚀 Ca## 🛠️ Desarrollo y Extensión

### Estructura de Módulos

- **`src/core/`**: Lógica de negocio pura, independiente de la UI
- **`src/gui/`**: Interfaz de usuario con Flet, componentes y vistas
- **`src/infrastructure/`**: Servicios transversales (config, logging)
- **`src/events/`**: Sistema de comunicación entre componentes

### Cómo Agregar Nueva Funcionalidad

1. **Lógica de negocio**: Añadir en `src/core/`
2. **Vista**: Crear en `src/gui/views/`
3. **Navegación**: Actualizar `main.py` y navigation rail
4. **Eventos**: Usar `EventDispatcher` para comunicación
5. **Configuración**: Añadir variables en `infrastructure/config.py`

--- **Simulación automática de ventas** cada X segundos configurable
* **Monitor en tiempo real** con historial de ventas recientes
* **Dashboard de estadísticas** con balance total y promedios
* **Arquitectura modular desacoplada** con separación core/gui/infrastructure
* **Preservación del estado** de las vistas (dropdowns, scroll, inputs)
* **Sistema de logging configurable** por entorno con rotación de archivos
* **Sistema de eventos pub/sub** para comunicación entre componentes
* **Navegación lateral** con cambio de vistas sin pérdida de estado

---

## 🧱 Estructura del Proyecto

### Estructura de Archivos
```
personal-expendio-2/
├── README.md                                    # Documentación del proyecto
├── requirements.txt                             # Dependencias de Python
├── logs/
│   └── expendio.log                            # Logs de la aplicación (generado)
├── src/                                        # Código fuente principal
│   ├── main.py                                 # Punto de entrada y aplicación principal
│   │
│   ├── core/                                   # 🏗️ Lógica de negocio central
│   │   ├── __init__.py                         # Exportaciones del módulo core
│   │   ├── data_store.py                       # Almacén en memoria del historial de ventas
│   │   └── updater.py                          # Generador de ventas automáticas
│   │
│   ├── events/                                 # 📡 Sistema de comunicación
│   │   ├── __init__.py                         # Exportaciones del módulo events
│   │   └── dispatcher.py                       # Publisher/Subscriber para eventos
│   │
│   ├── gui/                                    # 🎨 Interfaz de usuario (Flet)
│   │   ├── __init__.py                         # Exportaciones del módulo gui
│   │   ├── bindings.py                         # Vinculación reactiva datos ↔ UI
│   │   ├── views.py                            # Importaciones centralizadas de vistas
│   │   │
│   │   ├── components/                         # Componentes reutilizables
│   │   │   ├── __init__.py                     # Exportaciones de componentes
│   │   │   └── app_bar.py                      # Barra superior con estadísticas
│   │   │
│   │   └── views/                              # Vistas principales de la app
│   │       ├── __init__.py                     # Exportaciones de vistas
│   │       ├── balance_view.py                 # Vista de resumen y estadísticas
│   │       └── sales_view.py                   # Vista de monitor en tiempo real
│   │
│   ├── infrastructure/                         # ⚙️ Servicios transversales
│   │   ├── __init__.py                         # Exportaciones de infraestructura
│   │   ├── config.py                           # Sistema de configuración por variables ENV
│   │   └── logger.py                           # Logger avanzado con rotación de archivos
│   │
│   └── storage/                                # 💾 Directorios de almacenamiento
│       ├── data/                               # Datos persistentes (vacío por defecto)
│       └── temp/                               # Archivos temporales (vacío por defecto)
```

### Archivos Python por Módulo
```bash
# Listado real de archivos del proyecto
./src/main.py                                   # 🚀 Aplicación principal Flet
./src/core/__init__.py                          # Exportaciones: updater, data_store, logger
./src/core/config.py                            # ⚠️ Configuración legacy 
./src/core/data_store.py                        # 📊 Historial de ventas en memoria
./src/core/logger.py                            # ⚠️ Logger legacy
./src/core/updater.py                           # 🔄 Simulador automático de ventas
./src/events/__init__.py                        # Exportaciones: dispatcher
./src/events/dispatcher.py                      # 📡 Pub/Sub para eventos de la app
./src/gui/__init__.py                           # Exportaciones: views, bindings, components
./src/gui/bindings.py                           # 🔗 Vinculación reactiva UI ↔ datos
./src/gui/views.py                              # Importaciones centralizadas
./src/gui/components/__init__.py                # Exportaciones: AppBar
./src/gui/components/app_bar.py                 # 📊 Barra superior con contadores
./src/gui/views/__init__.py                     # Exportaciones: SalesView, BalanceView
./src/gui/views/balance_view.py                 # 📈 Vista de estadísticas y resumen
./src/gui/views/sales_view.py                   # 💰 Monitor de ventas en tiempo real
./src/infrastructure/__init__.py                # Exportaciones: config, logger
./src/infrastructure/config.py                 # ⚙️ Configuración centralizada (ENV)
./src/infrastructure/logger.py                 # 📝 Sistema de logging profesional
```

---

## 🏗️ Diagrama de Arquitectura

### Vista de Alto Nivel: Flujo de Datos y Comunicación

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          🎨 CAPA DE PRESENTACIÓN (GUI)                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌─────────────────┐    ┌─────────────────┐                │
│  │   AppBar     │    │   SalesView     │    │  BalanceView    │                │
│  │ (Contador)   │    │ (Monitor RT)    │    │ (Estadísticas)  │                │
│  └──────────────┘    └─────────────────┘    └─────────────────┘                │
│           │                    │                       │                        │
│           └────────────────────┼───────────────────────┘                        │
│                                │                                                │
│  ┌─────────────────────────────┼─────────────────────────────────────────────┐  │
│  │             📡 bindings.py (Vinculación Reactiva)                        │  │
│  │                             │                                            │  │
│  │  • bind_sales_to_view()     │     • initialize_view_data()              │  │
│  │  • bind_multiple_views()    │     • on_new_sale() callbacks             │  │
│  └─────────────────────────────┼─────────────────────────────────────────────┘  │
└─────────────────────────────────┼─────────────────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │ 📡 EVENT DISPATCHER      │
                    │ (Publisher/Subscriber)    │
                    │                          │
                    │ events/dispatcher.py     │
                    │ • subscribe()            │
                    │ • dispatch()             │
                    │ • unsubscribe()          │
                    └─────────────┬─────────────┘
                                  │
┌─────────────────────────────────┼─────────────────────────────────────────────────┐
│                       🏗️ CAPA DE LÓGICA DE NEGOCIO (CORE)                       │
├─────────────────────────────────┼─────────────────────────────────────────────────┤
│                                 │                                                │
│  ┌─────────────────┐           │           ┌─────────────────┐                  │
│  │   updater.py    │───────────┼──────────▶│  data_store.py  │                  │
│  │                 │           │           │                 │                  │
│  │ • start_simulation()        │           │ • add_sale()    │                  │
│  │ • genera ventas auto        │           │ • get_sales()   │                  │
│  │ • cada N segundos           │           │ • clear_sales() │                  │
│  │ • dispatch("SALE_ADDED")    │           │ • sales_history │                  │
│  └─────────────────┘           │           └─────────────────┘                  │
│           │                    │                      │                          │
│           │                    │                      │                          │
│  ┌─────────────────────────────┼──────────────────────┼─────────────────────┐    │
│  │                             │                      │                     │    │
│  │                           EMITE EVENTO             │                     │    │
│  │                             │                      │                     │    │
│  │                             ▼                      │                     │    │
│  │                   "SALE_ADDED"                     │                     │    │
│  │                             │                      │                     │    │
│  │                             │                      ▼                     │    │
│  │                             │              🗄️ HISTORIAL EN MEMORIA        │    │
│  │                             │                sales_history[]            │    │
│  └─────────────────────────────┼─────────────────────────────────────────────┘    │
└─────────────────────────────────┼─────────────────────────────────────────────────┘
                                  │
┌─────────────────────────────────┼─────────────────────────────────────────────────┐
│                     ⚙️ CAPA DE INFRAESTRUCTURA (SERVICES)                       │
├─────────────────────────────────┼─────────────────────────────────────────────────┤
│                                 │                                                │
│  ┌─────────────────┐           │           ┌─────────────────┐                  │
│  │    config.py    │           │           │    logger.py    │                  │
│  │                 │           │           │                 │                  │
│  │ • Config class  │           │           │ • setup_logger()│                  │
│  │ • Variables ENV │           │           │ • log_sale()    │                  │
│  │ • LOG_LEVEL     │           │           │ • rotación      │                  │
│  │ • SIM_INTERVAL  │           │           │ • archivo + console │              │
│  │ • MAX_HISTORY   │           │           │                 │                  │
│  └─────────────────┘           │           └─────────────────┘                  │
└─────────────────────────────────┼─────────────────────────────────────────────────┘
                                  │
                         ┌────────┴────────┐
                         │ 🚀 main.py      │
                         │                 │
                         │ • MainApp       │
                         │ • Navigation    │
                         │ • Flet setup    │
                         │ • Event loop    │
                         └─────────────────┘
```

### Flujo de Ejecución Detallado

```
🔄 SIMULACIÓN DE VENTAS:
┌─────────────────────────────────────────────────────────────────┐
│ 1. updater.start_simulation()                                  │
│    ├─ Genera venta aleatoria cada N segundos                   │
│    ├─ data_store.add_sale(sale)                               │
│    ├─ logger.log_sale(sale)                                   │
│    └─ dispatcher.dispatch("SALE_ADDED", sale) ────┐           │
└─────────────────────────────────────────────────────┼───────────┘
                                                      │
📡 PROPAGACIÓN DE EVENTOS:                             │
┌─────────────────────────────────────────────────────┼───────────┐
│ 2. dispatcher.dispatch("SALE_ADDED", sale)         │           │
│    └─ Llama a todos los callbacks suscritos ────────┼───────────┤
└─────────────────────────────────────────────────────┼───────────┘
                                                      │
🔗 ACTUALIZACIÓN REACTIVA:                             │
┌─────────────────────────────────────────────────────┼───────────┐
│ 3. bindings.on_new_sale(sale_data) ◄───────────────┘           │
│    ├─ current_sales = data_store.get_sales()                   │
│    ├─ view.update_sales(current_sales)                         │
│    └─ view.update_counters(total_sales, total_amount)          │
└─────────────────────────────────────────────────────────────────┘
                                    │
🎨 ACTUALIZACIÓN DE UI:              │
┌─────────────────────────────────────┼───────────────────────────┐
│ 4. Vistas se actualizan            │                           │
│    ├─ SalesView.update_sales() ◄───┼─ Lista de ventas         │
│    ├─ BalanceView.update_sales() ◄─┼─ Estadísticas            │
│    └─ AppBar.update_counters() ◄───┘─ Contadores globales     │
└─────────────────────────────────────────────────────────────────┘
```

### Patrones Arquitectónicos Implementados

1. **🏛️ Clean Architecture (Hexagonal)**
   - **Core**: Lógica de negocio pura (data_store, updater)
   - **GUI**: Adaptadores de UI (views, components, bindings) 
   - **Infrastructure**: Servicios externos (config, logger)

2. **📡 Publisher-Subscriber Pattern**
   - **Publisher**: `updater.py` emite eventos "SALE_ADDED"
   - **Subscribers**: Vistas suscritas vía `bindings.py`
   - **Event Bus**: `dispatcher.py` centraliza la comunicación

3. **🔗 Data Binding Reactivo**
   - **Unidireccional**: Datos fluyen de Core → GUI
   - **Automático**: Cambios en datos actualizan UI sin intervención manual
   - **Desacoplado**: UI no conoce directamente el modelo de datos

4. **🏭 Dependency Injection**
   - **Config**: Variables de entorno inyectadas vía `infrastructure/config.py`
   - **Logger**: Servicio inyectado en todos los módulos
   - **Loose Coupling**: Módulos no dependen de implementaciones concretas

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
