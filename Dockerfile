FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
