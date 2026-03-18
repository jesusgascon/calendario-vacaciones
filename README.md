# Calendario de Vacaciones - Sesame HR

Esta aplicación es un panel de control personalizado y avanzado para visualizar las vacaciones, ausencias y bajas de todo el equipo, utilizando la API interna de **Sesame HR**. Ofrece una experiencia más rica y filtrable que la interfaz estándar.

## 🚀 Cómo iniciar el proyecto

El proyecto funciona con un **servidor proxy local** escrito en Python que se encarga de saltarse las restricciones de CORS del navegador.

Para arrancarlo, simplemente ejecuta en tu terminal:

```bash
./start.sh
```

Esto levantará el servidor local en el puerto `8765` (`http://localhost:8765`) y abrirá tu navegador automáticamente.

## ✨ Características Principales

- **Dashboard Multivista Dinámico**: Cambia instantáneamente entre vistas de **Mes**, **Semana** o **Día**. La navegación se adapta automáticamente al periodo seleccionado.
- **Personalización de Marca (Branding)**: Posibilidad de configurar el nombre de la empresa, color corporativo y logo personalizado directamente desde la pantalla de configuración.
- **Contraste Inteligente**: El sistema ajusta automáticamente el brillo de tu color de marca cuando el **Modo Oscuro** está activo para garantizar una legibilidad perfecta.
- **Acceso LAN (Red Local)**: Soporta acceso a través de IPs locales (`192.168.x.x`, etc.) para que puedas consultar el calendario desde otros dispositivos de la oficina.
- **Filtro de Empleados Inteligente**: Buscador en tiempo real y contador de selección (ej. "Empleados (5/25)").
- **Exportación iCal/Google Calendar**: Descarga un archivo `.ics` o genera un enlace de suscripción para integrar las ausencias en tu calendario personal.
- **Auto-Login Multicreencial**: Gestiona varias empresas y recuerda tus credenciales de forma segura en `config.json`.

## 🧠 Arquitectura y Archivos

### `index.html` (Interfaz)
- Diseño responsivo con **Glassmorphism**.
- Sistema de modales para detalles diarios y configuración inicial.

### `app.js` (Lógica de Aplicación)
- Gestiona el estado global (`STATE`) y la reactividad de la UI.
- **Branding Engine**: Aplica colores y logos detectando el contraste óptimo.
- **Navigation logic**: Maneja los desplazamientos temporales según la vista activa.

### `styles.css` (Estilos)
- Temas dinámicos Claro/Oscuro mediante variables CSS.
- Animaciones sutiles y micro-interacciones.

### `server.py` (Backend Proxy)
- Actúa como puente para la API de Sesame y gestiona la lectura/escritura de `config.json`.
- Permite la sincronización de configuraciones entre dispositivos en la misma red.

## 🛠️ Mantenimiento

- **Cambio de Empresa**: Puedes añadir nuevas empresas o eliminar las existentes desde el panel lateral.
- **IP Local**: Si el servidor corre en `192.168.1.10`, puedes acceder desde cualquier otro PC de la red a esa misma dirección.

---
*Desarrollado para ofrecer una visión clara, rápida y estética del equipo.*
