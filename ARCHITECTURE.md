# 🏗️ Arquitectura Técnica - Sesame Premium Dashboard

Este documento detalla la ingeniería detrás del dashboard, centrándose en la resiliencia y el procesamiento de datos.

## 1. Estrategia de Conectividad Híbrida (Doble Servidor)

Para garantizar que el dashboard funcione incluso en entornos corporativos restrictivos o ante cambios en la API de Sesame, hemos implementado una **lógica de failover automático**:

- **Capa Primaria (Directa)**: Intenta conectar directamente con `api.sesametime.com` o `back-eu1.sesametime.com` usando cabeceras de navegador.
- **Capa Secundaria (Proxy)**: Si la primaria falla (error 403, CORS o red), la aplicación desvía la petición al servidor local `server.py`.
- **Ventaja**: Máxima velocidad cuando es posible, y fiabilidad total cuando es necesario.

## 2. Motor de Procesamiento de Datos (Normalization Layer)

La API de Sesame devuelve datos en múltiples formatos (REST estándar y BI Engine). El dashboard utiliza una capa de normalización que:
1. **Unifica**: Convierte estructuras anidadas de "Work Entries" en un modelo plano de `Signings`.
2. **Cruce (Smart Match)**: Cruza el calendario de ausencias (módulo `schedule/v1`) con los fichajes (`work-entries/v3`) en tiempo real.
3. **Rastreo de Origen (Device Context)**: Extrae y correlaciona metadatos de dispositivo (`origin`) desde el motor BI y objetos `checkIn/checkOut` para monitorizar el canal de entrada (Web, Móvil, Tablet).
4. **Validación**: Detecta inconsistencias (fichajes en días de vacaciones, falta de marcaje de salida) antes de renderizar la UI.
5. **Incidence Detection Engine (v1.4.0)**: Capa de auditoría que realiza peticiones paralelas a los endpoints de la REST API (`/api/v3/check-incidences`, `/api/v3/work-entry-requests`) para interceptar solicitudes de borrado o edición que el motor de BI aún no ha consolidado. Realiza un *fuzzy match* por ID y timestamp para garantizar la integridad de los balances horarios.

## 3. Monitorización de Presencia en Vivo (Radar)

El radar de disponibilidad funciona mediante un sondeo optimizado a la ruta `/api/v3/work-entries/presence`:
- **Estado Local**: La aplicación mantiene un mapa de IDs de empleados vinculados a sus fotos y nombres.
- **Difusión**: El estado se propaga a tres puntos de la interfaz simultáneamente: la barra lateral, el resumen de cabecera y el panel de fichajes.

## 4. Seguridad y Persistencia

- **Configuración Segura (Split Strategy)**: Implementamos una arquitectura de dos archivos para proteger los datos:
  - `config.json`: Metadatos públicos de empresas.
  - `config.secrets.json`: Tokens USID y secretos de autenticación (ignorado por Git).
- **Fusión en Memoria**: El servidor Python (`server.py`) fusiona ambos archivos en tiempo de ejecución, proporcionando una vista unificada al frontend sin exponer secretos en el repositorio.

## 5. Capa de Persistencia y UX

La aplicación minimiza la fricción del usuario mediante una gestión de estado persistente:
- **LocalStorage**: Almacena el tema (Light/Dark), el estado de colapso de la sidebar y, desde la v1.4.0, el **módulo activo**.
- **SessionStorage**: Mantiene la fecha de navegación actual para que el usuario no pierda el contexto temporal al navegar entre vistas.

## 6. Visual Stack

- **Motor UI**: Vanilla Javascript (ES6+). Sin frameworks pesados para garantizar una carga instantánea.
- **Diseño**: CSS3 moderno con variables dinámicas, Flexbox y Grid Layout de alta densidad.
- **Componentes**: Arquitectura basada en módulos (`FichajesModule`, `VacacionesModule`) para facilitar la mantenibilidad.

---
*Este proyecto demuestra cómo extender una plataforma SaaS cerrada mediante ingeniería inversa y capas de valor añadido sobre su API.*
