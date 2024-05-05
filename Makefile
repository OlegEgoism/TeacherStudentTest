makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

run:
	python manage.py runserver

build:
	sudo docker build -t tst .

drun:
	sudo docker run -p 8000:8000 tst
