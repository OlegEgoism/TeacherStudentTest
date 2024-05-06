# Используем образ Python версии 3.10
FROM python:3.10-alpine3.14

# Устанавливаем переменную окружения для Python, чтобы вывод был приятным
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файлы requirements.txt в /app
COPY . .

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
