# 🗓️ Sesame Premium Dashboard

Un dashboard de alta fidelidad, inteligencia operativa y monitorización avanzada para **Sesame HR**. Diseñado para centralizar la gestión de vacaciones, ausencias de calendario y registros de actividad real en una interfaz panorámica y verdaderamente profesional. Ha sido diseñado como un proyecto integral de front/back (SPA + Proxy Local) para mejorar la usabilidad técnica de recursos humanos.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Frontend](https://img.shields.io/badge/frontend-JS%20Vanilla-yellow.svg)
![Backend](https://img.shields.io/badge/backend-Python%20Proxy-green.svg)
![Status](https://img.shields.io/badge/status-Stable-success.svg)

---

## 🌟 Resumen de Módulos (Core Features)

La aplicación está dividida en dos pilares o módulos fundamentales, pensados para proveer tanto supervisión gerencial como asistencia técnica de primer nivel.

### 1. 📡 Radar de Disponibilidad, Presencia y Fichajes
Este módulo sustituye al tradicional panel de marcajes en un panel tipo "Torre de Control".
- **Monitorización en Tiempo Real "Live"**: Visualiza quién está trabajando, quién está en pausa y quién está ausente en el mismo instante, extrayendo datos directos invisibles de la API de SesameHR.
- **Indicadores Visuales y Semáforos**: Semáforos de estado (Verde / Ámbar / Rojo) que fluyen por todo el DOM, acoplándose al árbol dom del listado de empleados en el Sidebar.
- **Resumen Ejecutivo Inmediato**: Un contador sumatorio visual interactivo que permite saber de un simple vistazo "Cuántos faltan", "Cuántos están en descanso", cruzando dicha información frente a las jornadas planeadas.
- **Detección Automática de Incidencias**: El aplicativo lee los fichajes en vivo e identifica heurísticamente "salidas sin marcar", "turnos partidos no cerrados" y "potencial de horas extras".

### 2. 🧠 Calendario de Inteligencia Operativa y Vacaciones
Abstrae la lectura manual de solicitudes en una parrilla inmensa y predictiva.
- **Procesador de "Smart Match" (Cruce)**: Un motor JS local que conecta calendarios de ausencia autorizados (`schedule/v1`) con los marcajes del entorno fichajes (`work-entries/v3`), alertando de conflictos directos "el usuario trabajó un día festivo" o "estuvo ausente sin solicitud".
- **Balance Total Anual Calculado**: Algoritmos autónomos averiguan los días totales según contrato vs tomados actualmente.
- **Vista de Cuadrícula (Mes/Semana/Día)**: Escalado panorámico renderizado usando Flexbox Dinámico, asegurando no sufrir ralentizaciones aun cargando múltiples cientos de empleados.
- **Sincronización ICS Externa**: Habilidad directa de exportación para Outlook o Google Calendars, sirviendo como Feed permanente directo.

---

## 🛠️ Experiencia Premium (UI/UX)
El producto base fue desarrollado bajo los estándares más restrictivos de usabilidad visual de cara a pantallas gerenciales ultra anchas o salas de mando técnica (Kiosko Mode).
- **Motor de Theming Dual**: Incorpora tanto Modo Claro (Light) como Oscuro (Dark) alterando tokens de diseño locales utilizando abstracciones de Glassmorphism.
- **Diseño Ultra-Denso**: Priorización total a la colocación y visualización del dato.
- **Sidebars Responsivos**: Capacitados para comprimir y colapsarse, manteniendo los identificadores colorímetricos primarios (Ausencias con colores hash MD5).

---

## 🚀 Guía de Instalación y Primeros Pasos

El proyecto consta de una capa cliente ligera (`app.js`) y un servidor en Python (`server.py`).

### Requisitos previos fundamentales
- **Python 3.8+** (Instalado globalmente o en Entorno Virtual).
- **Conectividad Mínima** a internet para poder descargar de CDN las fuentes ("JetBrains Mono", "Plus Jakarta Sans") y la pequeña librería de gráficos (Chart.js).

### Descarga e Inicialización
1. Clona el repositorio desde GitHub de forma local.
2. Gestiona tu configuración (El sistema es "multi-compañía"):
   - Copia o duplica el archivo `.example` a sus homólogos ocultos.
   - `cp config.example.json config.json`
   - `cp config.secrets.example.json config.secrets.json`
3. Ejecuta el Proxy Bridge Local
   - Usando el empaquetador Unix: `bash start.sh`
   - O usando el núcleo nativo de sistema: `python3 server.py`
4. El script está configurado para "robar el foco" y abrir el dashboard en tu navegador predeterminado automáticamente: `http://localhost:8765`. 

### Autenticación e Inserción de Tokens
No existe pantalla de login clásico, utilizamos un puente JWT y extracción web.
Las credenciales secretas no deben empujarse nunca (`.gitignore`), así que tienes un script extra que roba validamente la cookie si la desconoces.
`python3 get-token.py`. El sistema imprimirá instrucciones.

---

## 🛡️ Arquitectura Técnica y Abstracción de WAF (Web Application Firewall)

A nivel de software e ingeniería de redes, este producto fue desarrollado con metodologías de *Bypass Web* ya que sistemas como el Bi-Engine de Sesame están fuertemente protegidos.
**Principios fundamentales de nuestra arquitectura**:
1. **Doble Servidor de Fallback**: Si las conexiones en Javascript Puro y en bruto (Direct llamadas Fetch a URLs remotos) decaen por bloqueos de CORS, la app reintenta de inmediato pasando por tu BackEnd local (`/sesame-api/`).
2. **Proxy Spoofing**: El Python levanta las políticas HTTP para mimetizarse simulando un agente estándar como "Chrome 120" en un PC Windows.
3. **Escudo de Estado**: Todos los diccionarios, IDs e Imágenes se mantienen almacenados y deduplicados en el objeto `STATE` (singleton global) de JS, minimizando llamadas excesivas a red.

> **Consulte el archivo profundo:** Para ver ejemplos de cómo las matrices y los diccionarios cruzan los balances, lee detenidamente nuestro [ARCHITECTURE.md](./ARCHITECTURE.md).

---

## 🔐 Seguridad e Integridad de Repositorio (Publicación en Github)

Este repositorio es agnóstico del despliegue, todo está anonimizado.
- Ningún archivo local `.json` a excepción de los `.example` se suben jamás hacia los remotos. Tu información corporativa e `ids` quedan relegados a tu máquina.
- Queda totalmente proscrita la automatización de la integración de configuraciones privadas.

## 📄 Licencia y Credenciales
Construido y mantenido activamente para despliegues cerrados. Totalmente cobijado bajo la Licencia **MIT**.

---
*Desarrollado para optimizar la visibilidad y el control operativo en entornos cerrados y corporativos de Sesame HR.*
