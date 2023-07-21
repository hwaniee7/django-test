FROM python:3.11.4-slim-bullseye as build-stage
WORKDIR /app
RUN apt-get update \
    && rm -rf /var/lib/apt/lis ts/*
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "manage.py", "runserver"]
CMD ["0.0.0.0:8000"]