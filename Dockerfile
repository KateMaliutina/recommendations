# Базовый образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Открываем порт для сервера
EXPOSE 80

# Устанавливаем дополнительную утилиту
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc
RUN apt install -y netcat-traditional

# Делаем скрипт исполняемым
RUN chmod +x entrypoint.sh

# Запуск приложения
CMD ["./entrypoint.sh"]
