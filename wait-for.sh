#!/bin/sh
# wait-for.sh

host="$1"
shift
cmd="$@"

until nc -z "$host" 3306; do
  echo "Esperando a que MySQL ($host:3306) esté disponible..."
  sleep 2
done

echo "MySQL está listo, ejecutando comando..."
exec $cmd
