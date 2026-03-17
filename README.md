# Calendario de Vacaciones - Sesame HR

Esta aplicación es un panel de control personalizado y avanzado para visualizar las vacaciones, ausencias y bajas de todo el equipo, utilizando la API interna de **Sesame HR**. Ofrece una experiencia más rica y filtrable que la interfaz estándar.

## 🚀 Cómo iniciar el proyecto

El proyecto funciona con un **servidor proxy local** escrito en Python que se encarga de saltarse las restricciones de CORS del navegador.

Para arrancarlo, simplemente ejecuta en tu terminal:

```bash
./start.sh
```

Esto levantará el servidor local en el puerto `8766` (`http://localhost:8766`) y abrirá tu navegador automáticamente. Nota: La aplicación redirige internamente a `http://localhost:8765` para el dashboard principal.

## ✨ Características Principales

- **Dashboard Multivista**: Calendario (mes/semana), vista por empleado y estadísticas detalladas.
- **Filtro de Empleados Inteligente**: Buscador en tiempo real y contador de selección (ej. "Empleados (5/25)").
- **Filtro Automático de Ausencias**: La barra lateral oculta automáticamente los tipos de ausencia que no tienen registros en el periodo actual.
- **Exportación iCal/Google Calendar**: Descarga un archivo `.ics` con todas las ausencias visibles para integrarlas en tu calendario personal.
- **Modo Oscuro/Claro**: Cambio de tema instantáneo con persistencia en el navegador.
- **Auto-Login**: Recuerda tus credenciales (Token USID y Company ID) de forma segura en un archivo local `config.json`.

## 🧠 Arquitectura y Archivos

### `index.html` (Estructura)
- Dashboard con diseño responsivo basado en CSS Grid y Flexbox.
- Contiene los modales de detalle y el sistema de navegación entre vistas.

### `app.js` (Cerebro)
- Gestiona el estado global (`STATE`), las llamadas a la API y el renderizado dinámico.
- **Logic Key**: Cruza los IDs de ausencia con los nombres reales de Sesame para evitar etiquetas genéricas.
- **Exportación**: Genera el contenido del calendario siguiendo el estándar RFC 5545 (iCalendar).

### `styles.css` (Diseño)
- Estética moderna con efectos de cristal (glassmorphism) e interactividad suave.
- Soporta temas dinámicos mediante variables CSS (`:root`).

### `server.py` (Backend)
- Proxy para peticiones API y servidor de archivos estáticos. Maneja la persistencia de la configuración.

### `get-token.py` (Utilidad)
- Script auxiliar para facilitar la extracción del token `USID` del navegador.

## 🛠️ Mantenimiento

- **Token Caducado**: Si la app deja de cargar datos, actualiza el valor de la cookie `USID` en `config.json`.
- **Nuevos Tipos de Ausencia**: Se cargan automáticamente desde la API de Sesame.

---
*Desarrollado para ofrecer una visión clara y rápida del equipo.*
