#!/bin/sh

# Espera a que el host:puerto esté disponible antes de continuar
# Uso: ./wait-for.sh host:port -- comando_a_ejecutar

set -e

hostport="$1"
shift

host="$(echo "$hostport" | cut -d: -f1)"
port="$(echo "$hostport" | cut -d: -f2)"

until nc -z "$host" "$port"; do
  echo "Esperando a que $host:$port esté disponible..."
  sleep 2
done

exec "$@"
