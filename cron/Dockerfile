FROM alpine:latest

# Установка необходимых утилит
RUN apk add --no-cache curl

# Скачивание актуальной версии Supercronic (пример для v0.2.49)
ENV SUPERCRONIC_URL=https://github.com \
    SUPERCRONIC=supercronic-linux-amd64

RUN curl -fsSLO "$SUPERCRONIC_URL" \
    && chmod +x "$SUPERCRONIC" \
    && mv "$SUPERCRONIC" "/usr/local/bin/supercronic"

WORKDIR /app
COPY crontab /app/crontab

# Запуск Supercronic
CMD ["supercronic", "/app/crontab"]
