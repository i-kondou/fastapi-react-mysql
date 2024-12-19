FROM python:3.11
ENV PYTHONUNBUFFERED=1

WORKDIR /app_backend

COPY /backend_Project/docker/python/requirements.txt /app_backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app_backend/requirements.txt

COPY /backend_Project/backend /app_backend/backend/

CMD ["uvicorn", "backend.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]