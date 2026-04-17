# 🌿 Guía Universal de Contribución al Proyecto

¡Bienvenido! Estamos encantados de que quieras contribuir al **Sesame Premium Dashboard**. 
Para garantizar que nuestro código, nuestra infraestructura Zero-Trust y nuestros flujos de interfaz permanezcan fiables al 100%, todos los colaboradores deben seguir estrictamente esta guía técnica de contribución.

---

## 1. El Paradigma Fundamental

Este proyecto NO es un monolito empresarial tradicional; es una herramienta de bypass e interfaz visual de alto rendimiento (HOC - High Order Client).
Nuestra regla cardinal de oro: **NUNCA utilices herramientas de terceros ni librerías pesadas si no es absoluta y terminalmente necesario.**
- 🚫 Nada de React.js, Angular, ni Vue. Empleamos iteración de Vanilla JS (`DOM.getElementById`). Re-pintamos lo mínimo necesario.
- 🚫 Nada de TailwindCSS precompilado que engorde el bundle. Disponemos de nuestras propias directrices Token `styles.css`.
- 🚫 Excluidas grandes librerías de backend SQL u ORMs. Los ficheros JSON locales actúan de State persistence.

---

## 2. Metodología Inquebrantable de Control de Versiones

Jamás hagas push al repositorio remoto de material sensible. El proyecto está preparado para manejar multi-clientes.
Al iniciar deberás instalar tus perfiles:
1. Las configuraciones vivas residen en `config.json` y `config.secrets.json`.
2. Estas deben vivir SOLO localmente. Tienen `ignores` persistentes aplicados en `.gitignore`.
3. Cualquier cambio estructural en la manera en que solicitamos un JSON de configuración, debe ser reflejado alterando `config.example.json`.
4. El `.gitignore` es el escudo de tu empresa frente a infracciones de leyes de protección de datos (GDPR). **Jamás lo elimines ni sortees su bloqueo con el comando `--force`**.

## 3. Pull Requests y Aprobaciones

1. Haz un Fork y crea una rama descriptiva (`feature/live-widget` o `fix/cors-rejection`).
2. Verifica que `server.py` pasa los lint propios estándar de Python (PEP 8). Limita los saltos de línea y verifica el manejo de Excepciones. El Proxy NO puede hacer 'panic' y caer; ante un JSON erróneo devolverá un 502 al Frontend, pero el Proxy interno en el puerto 8765 debe seguir respirando.
3. Envía tu PR y asegúrate de mencionar qué sección estructural del DOM fue modificada.
4. OBLIGATORIO: Documenta masivamente cualquier adición dentro del archivo usando docstrings (si es Python) o delimitadores de comillas (si es Javascript). El código sin mapa documental es código huérfano.

## 4. Testing End-to-End Visual

Para depurar en modo Kiosko sin datos limpios de Sesame:
Limpia todos los JSON enviando un array vacío y fíjate si la UI devuelve o crashea un array _OutOfBoundsException_. La "Setup Screen" (`#setup-screen`) de validación debe proteger cualquier acceso indebido.

**¡Gracias por mantener el proyecto vivo, brillante y corporativo!**
