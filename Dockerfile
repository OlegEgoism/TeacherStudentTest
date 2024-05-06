# Используем образ Python версии 3.10
FROM python:3.10-alpine3.14

# Устанавливаем переменную окружения для Python, чтобы вывод был приятным
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файлы requirements.txt в /app
COPY requirements.txt /app/

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога в /app
COPY . /app/

# Выполняем миграции
RUN python manage.py makemigrations
RUN python manage.py migrate

# Экспортируем порт 8000, который будет прослушиваться внутри контейнера
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
