FROM python:3.11-slim

# Instalar netcat
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for.sh

CMD ["sh", "-c", "./wait-for.sh db:3306 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
