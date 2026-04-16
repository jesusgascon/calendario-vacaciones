# 🏗️ Arquitectura Técnica - Sesame Premium Dashboard

Este documento detalla los componentes técnicos, el flujo de datos y los algoritmos principales que hacen funcionar este dashboard.

## 1. Diseño de Arquitectura

El sistema utiliza un patrón de **Proxy Local**. Dado que la API de Sesame HR tiene restricciones de CORS (Cross-Origin Resource Sharing) estrictas para navegadores, este proyecto utiliza un servidor Python intermedio.

### Flujo de Datos
1. **Cliente (JS)**: Solicita datos a `/sesame-api/v3/attendance/...`
2. **Servidor (Python)**: Recibe la petición, adjunta las cookies de sesión guardadas en `config.json` y la reenvía a `back-eu1.sesametime.com`.
3. **API Sesame**: Responde al servidor Python.
4. **Servidor (Python)**: Devuelve la respuesta íntegra al Cliente.

## 2. Gestión de Estado (Frontend)

La aplicación es una **SPA (Single Page Application)** escrita en Vanilla Javascript. El estado global se centraliza en el objeto `STATE` dentro de `app.js`:

```javascript
const STATE = {
  currentDate: new Date(),
  companies: [],
  companyId: null,
  theme: 'dark',
  // ... otros datos de vista
};
```

## 3. Algoritmo de Smart Match (Fichajes y Ausencias)

Una de las funcionalidades más avanzadas es el cruce automático de datos. El algoritmo reside en la función `parseRealSignings`.

### Proceso:
1. **Recolección**: Se obtienen los `entries` (fichajes reales) y los `absenceSegments` (segmentos de ausencia del calendario) para un empleado y día concreto.
2. **Cruze Temporal**: Para cada tramo de fichaje (Entrada -> Salida), el sistema comprueba si existe una ausencia en el calendario que se solape en ese rango horario.
3. **Etiquetado Inteligente**: 
    - Si hay solapamiento, el tramo de "Trabajo" se reclasifica automáticamente con el motivo de la ausencia (ej: "Gestión Privada").
    - Se calcula la duración exacta entre cada entrada y salida técnica.
4. **Renderizado**: Los datos procesados alimentan tanto la línea de tiempo (`timeline-bar`) como la tabla de detalles técnicos.

## 4. Motor de Temas Dinámico

El sistema de temas utiliza **Variables CSS** nativas. El cambio de tema se aplica mediante el atributo `data-theme` en el elemento raíz:

- **Estrategia**: Todas las capas de color (fondos, bordes, sombras) están vinculadas a variables como `--bg-card` o `--text-primary`.
- **Sincronización**: Al cambiar el tema, se disparan eventos de re-renderizado para los componentes que dependen de cálculos de color dinámicos (como gráficos o sombras dinámicas).

## 5. Almacenamiento y Seguridad

- **Configuración**: Las credenciales se almacenan localmente en `config.json`.
- **Sesión**: El sistema gestiona las cookies de sesión de forma transparente a través de los scripts `get-token.py` (para login interactivo) y `server.py` (para persistencia).

---
*Para desarrolladores: Se recomienda mantener la estructura de módulos (`MODULES.vacaciones`, `MODULES.fichajes`) para futuras expansiones de la interfaz.*
