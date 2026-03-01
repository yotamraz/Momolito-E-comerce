FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

# shared library will be mounted or copied at /shared
ENV PYTHONPATH=/app:/shared

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
