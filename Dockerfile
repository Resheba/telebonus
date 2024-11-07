FROM python:3.11.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code

COPY . .

CMD ["python", "-m", "src.main"]
