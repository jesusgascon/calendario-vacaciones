#!/bin/bash
# ==============================================================================
#  SESAME PREMIUM DASHBOARD - SHELL EXECUTOR MODULE
# ==============================================================================
#  Archivo: start.sh
#  Propósito: Hombro de ejecución universal compatible con sistemas POSIX (Linux/MacOS).
#  Maneja contextos de directorios y previene que el programa arranque des-orientado
#  si es llamado mediante un enlace simbólico, atajo local o un `cron` automático.
#
#  Opciones Válidas de Subcomandos CLI:
#    $ ./start.sh              -> Ejecuta directamente el entorno web de servidor HTTP proxy en el puerto por defecto (8765)
#    $ ./start.sh token        -> Salta el proceso de renderizado y arranca el Micro-Listener para robar/adquirir JWT Cookies
#    $ ./start.sh login        -> Alias de token
#    $ ./start.sh credentials  -> Alias de token
# ==============================================================================

# PASO 1: Orientación espacial del entorno (Hard-Resolution)
# Averigua dinámicamente cuál es el directorio real padre independientemente
# de la procedencia del bash invocador. 
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Desplazamos el scope al directorio detectado, garantizando que comandos python dependencias lean `config.json` exitosamente en el subyacente.
cd "$DIR"

# PASO 2: Router Argumental CLI.
# Intercepta el primer argumento de entrada "$1" pasado al script de BASH.
case "$1" in
  token|credentials|login)
    echo ""
    echo "============================================================"
    echo "🔑 MODO EXTRACCIÓN: Sistema Inteligente de Credenciales"
    echo "============================================================"
    echo "Lanzando el puente TCP hacia get-token.py... "
    echo "Prepara tu navegador Web."
    python3 get-token.py
    ;;
  *)
    echo ""
    echo "============================================================"
    echo "📅 MODO DASHBOARD: Arrancando Proxy Inverso y Visor"
    echo "============================================================"
    echo "Cargando componentes estructurales y levantando servidor HTTP..."
    python3 server.py
    ;;
esac
