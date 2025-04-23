FROM python:3.9-slim

WORKDIR /app

COPY backend/ backend/
COPY frontend/ frontend/
COPY database/ database/

RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt && \
    pip install -r frontend/requirements.txt

EXPOSE 5000 8501

CMD ["sh", "-c", "python backend/app.py & streamlit run frontend/app.py --server.port 8501 --server.enableCORS false"]
