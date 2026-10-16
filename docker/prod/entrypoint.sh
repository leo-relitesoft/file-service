set -e

APP_PORT="${APP_PORT:-443}"
TLS_ENABLED="${TLS_ENABLED:-true}"

if [ "$TLS_ENABLED" = "true" ]; then
  exec uv -q run -- uvicorn notificationsservice.main:app \
    --host 0.0.0.0 \
    --port "$APP_PORT" \
    --ssl-certfile="${TLS_CERT_FILE:-/etc/tls/certificate.crt}" \
    --ssl-keyfile="${TLS_KEY_FILE:-/etc/tls/private.key}"
fi

exec uv run fastapi run src/files/main.py --host 0.0.0.0 --port "$APP_PORT"
