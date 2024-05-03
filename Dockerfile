# Используем образ Python версии 3.8
FROM python:3.8

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

# Экспортируем порт 8000, который будет прослушиваться внутри контейнера
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
