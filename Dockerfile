FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY tests/ ./tests/

EXPOSE 5000

ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production
ENV PORT=5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]