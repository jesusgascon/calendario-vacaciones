#!/bin/bash
# ============================================================
#  start.sh — Lanzador de Sesame Premium Dashboard
#  Uso: ./start.sh          → inicia el servidor  
#       ./start.sh token    → primero extrae el token
# ============================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

case "$1" in
  token|credentials|login)
    echo "🔑 Extrayendo credenciales de Sesame HR..."
    python3 get-token.py
    ;;
  *)
    echo "🚀 Iniciando Sesame Premium Dashboard..."
    python3 server.py
    ;;
esac
