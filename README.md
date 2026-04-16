# 🗓️ Sesame Premium Dashboard

Un dashboard de alta fidelidad y monitorización avanzada para **Sesame HR**. Diseñado para centralizar la gestión de vacaciones, ausencias de calendario y registros de actividad real en una interfaz panorámica, técnica y profesional.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Frontend](https://img.shields.io/badge/frontend-JS%20Vanilla-yellow.svg)
![Backend](https://img.shields.io/badge/backend-Python%20Proxy-green.svg)

## ✨ Características Principales

### 📊 Dashboard de Fichajes (Módulo de Actividad)
- **Cruce Inteligente (Smart Match)**: Cruza automáticamente tus ausencias programadas (médico, gestión privada, baja) con los registros de fichaje para proporcionar un reporte de tiempo preciso.
- **Tabla Técnica de Alta Densidad**: Visualiza horarios, duraciones exactas (h/m), tipo de actividad y ubicación de cada tramo.
- **Timeline de Actividad**: Vista panorámica del día con indicadores visuales de Trabajo, Pausas y Ausencias detectadas.
- **Exportación Directa**: Generación de reportes en formato CSV para gestión administrativa.

### 📅 Gestión de Vacaciones y Ausencias
- **Vistas Múltiples**: Navegación por Mes, Semana y Día.
- **Resumen Estadístico**: Monitorización de horas trabajadas vs teóricas del mes.
- **Filtros Avanzados**: Filtrado por empleado y tipo de ausencia.
- **Multicompañía**: Soporte para gestionar múltiples perfiles de empresa de forma sencilla.

### 🎨 Experiencia de Usuario Premium
- **Motor de Temas**: Soporte completo para **Modo Claro** y **Modo Oscuro** sincronizado en todas las secciones.
- **Estética Empresarial**: Diseño compacto basado en grid, con sombras de profundidad y tipografía de precisión técnica.
- **Reactividad**: Filtrado y búsqueda instantánea de empleados.

## 🚀 Instalación Rápida

### Requisitos previos
- Python 3.8 o superior instalado.

### Configuración
1. Clona el repositorio (o descarga los archivos).
2. Abre una terminal en la carpeta del proyecto.
3. El proyecto no requiere dependencias externas pesadas, funciona con la librería estándar de Python.

### Ejecución
Usa el script de inicio proporcionado:
```bash
bash start.sh
```
O manualmente:
```bash
python3 server.py
```
Accede a la aplicación en: `http://localhost:8765`

## 🛠️ Arquitectura Técnica

El proyecto se divide en dos capas principales:
1. **Frontend (HTML5/CSS3/Vanilla JS)**: Gestiona toda la lógica de visualización, gestión de estado local y el algoritmo de emparejamiento de fichajes.
2. **Backend (Python Proxy)**: Actúa como puente para evitar problemas de CORS y centralizar las cookies de sesión de Sesame HR, permitiendo una comunicación segura con la API oficial.

Para más detalles sobre el funcionamiento interno, consulta el archivo [ARCHITECTURE.md](./ARCHITECTURE.md).

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---
*Desarrollado con ❤️ para optimizar la gestión de equipos en Sesame HR.*
