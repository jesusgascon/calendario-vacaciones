# 🏗️ Diseño y Arquitectura Técnica - Sesame Premium Dashboard

Este documento detalla exhaustivamente las metodologías, estrategias de ingeniería de software y decisiones técnicas que rigen el dashboard, concebido ex-profeso para maximizar la resiliencia operativa y la manipulación segura de datos masivos.

---

## 1. Topología del Sistema: Estrategia de Conectividad Híbrida (Doble Capa de Red)

Dada la agresividad del Web Application Firewall (WAF) que protege los entornos base de SesameHR y sus restricciones impuestas sobre CORS para conexiones de origen dispar, el cliente ha implementado un patrón de arquitectura denominado **Client-side Interceptor con Fallback Proxy**.

1. **Capa Primaria (Conexión Directa)**:
   - Operativa: La API Client Javascript nativa lanza peticiones XHR/Fetch directamente a `https://back-eu1.sesametime.com`.
   - Propósito: Minimizar latencias si el proveedor permite el origen temporalmente o al utilizarse en red local autorizada.
2. **Capa Secundaria / Proxy Engine (Redireccionamiento en localhost)**:
   - Cuándo se ejecuta: Automáticamente en caso de rechazos tipo HTTP 403, 404 estricto, o bloqueos por políticas CORS (`TypeError: Failed to fetch`).
   - Cómo opera: Todas las peticiones mutan su cabecera hacia `http://localhost:8765/sesame-api/...`. Allí nuestro micro-servidor de Python escrito explícitamente reempaqueta los _headers_ simulando un navegador Chrome (User-Agents, Referers) y vuelve a enviarlo originando el flujo local desde servidor hacia servidor (Server-To-Server Call), abatiendo la restricción de dominiatura.

---

## 2. Motor de Procesamiento (Data Normalization Layer) API

Las respuestas de la base Sesame se caracterizan por ser JSON asíncronos profundamente embebidos (Nested JSON), mezclando APIs legacy REST (`/v1`) con BI Engine analíticos (`/v3`). Nuestro backend/frontend no muestra la data cruda, requiere un pre-procesado intensivo.

### 2.1 Módulo del Cuadrante (Smart Match de Ausencias y Fichajes)
- Unifica las ramificaciones matriciales de `calendar-types` transformándolo en un _hash map_ de índice simple (`O(1)`) organizado por `ID_de_Empleado` -> `RangoDías`.
- Cruza en tiempo real ese hashmap de vacaciones aprobadas/ausencias con la tabla base de `work-entries/v3` (fichajes en vigor). Mapeando qué empleado hizo clics (Entries) y confrontándolo para destapar violaciones del protocolo (Como "Ausencia sin solicitud").

### 2.2 Recomputación Total Automática (Vacation Balance Override)
- A menudos ciertos usuarios sufren des-sincronizaciones con el contador visual y su total devengado. La SPA esquiva el total y calcula el devengado directamente haciendo un parsing masivo de todas las jornadas, calculando la diferencia y devolviendo el saldo autocalculado fiable.

---

## 3. Monitorización Radar Inteligente (Live State Management)

No consumimos WebSockets por limitación tecnológica del servicio provisto, logramos "Live Presence" estructurando ráfagas de PULL Requests inteligentes.

- **Políticas de Rate Limit**: En lugar de masacrar `/work-entries`, se sondea secuencialmente y bajo un retraso escalonado. Se almacenan perfiles e imágenes globalmente en la clase Map estática local para no descargar n-veces la URL de la misma imagen de usuario. Solo los statuses mutables (Trabajando, Online, Pause) son cruzados.
- **Dom-Binding**: Se usa Vanilla Javascript inyectando tokens de string interpolado limitando drásticamente el re-paint/re-flow. El árbol de elementos nunca se recrea, sino que navega el identificador CSS. El DOM solo es tocado si el _Hash MD5_ local del estado diverge del _Payload_.

---

## 4. Perspectivas de Autenticación Invisible y Seguridad (Zero-Trust Boot)

El despliegue está concebido bajo Zero-Trust, el Dashboard carece de base de datos SQL porque todo recae en la nube.
- **Configuraciones Aisladas**: La arquitectura demanda separar metadatos de configuración corporativa (logotipo, branding y UI en `config.json`) de los secretos duros (Bearer Tokens o JWT Cookies en `config.secrets.json`).
- Si fallase el _cold-boot_, el Dashboard incrusta el script alternativo `get-token.py`. Un mini-servidor local con código inyectable (`javascript:()`) que reescribe prototipos en el cliente original oficial roba y absorbe el Token de Sesión vivo de la API con seguridad plena y reinicia tu nodo local con ello.

---

## 5. Visual Rendering Architecture y Abstracciones CSS (Theming)

### 5.1 Glassmorphism Nativo
Se han eliminado dependencias pesadas visuales que limitaban la carga, implementándose:
1. `backdrop-filter: blur(24px)` para aislar el Canvas.
2. Contenedores SVG "Blobs" paralelos que flotan detrás del DOM principal alterando visualmente el espacio por efecto refractivo, atados mediante KeyFrames.

### 5.2 Responsive CSS Variables
Las variables `--step` se adaptan por escalado relativo `rem` garantizando visualización nativa independientemente de que se abra la aplicación en una tablet vertical, un kiosko 4K de recursos humanos o portátiles 1080p. 
El modo `[data-theme="light/dark"]` sobre el nodo `html` recalcula los backgrounds, bordes y sombras nativas dinámicamente (`window.localStorage.getItem("theme")`).

---
*Este documento conforma la guía arquitectónica universal para mantenimiento, validando por qué "Menos librerías y mayor reestructuración de conectores manuales" provee un resultado de fiabilidad y rendimiento absoluto.*
