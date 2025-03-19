# Use a lightweight Python image
FROM python:3.11-slim

# Install FastAPI and Uvicorn
RUN apt update && apt install -y netcat-openbsd postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn sqlalchemy asyncpg psycopg2-binary pandas
# Copy the application code
COPY main.py /app/main.py
COPY db_init.py /app/db_init.py
COPY models.py /app/models.py
COPY insert_data.py /app/insert_data.py
COPY db.py /app/db.py
# Set the working directory to /app
WORKDIR /app
# Expose UDS path as a volume
VOLUME ["/tmp"]
# Run Uvicorn using the Unix Domain Socket
#CMD ["uvicorn", "main:app", "--uds", "/tmp/service_b.sock"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


