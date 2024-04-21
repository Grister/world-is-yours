FROM python:3.8

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY store/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в контейнер
COPY . .

# Для Celery необходимо указать команду запуска
CMD ["celery", "-A", "store", "worker", "--loglevel=info"]
