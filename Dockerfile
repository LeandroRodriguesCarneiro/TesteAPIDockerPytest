FROM python:3.13.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ENV=development
ENV FLASK_APP=app.main:create_app
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
