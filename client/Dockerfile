FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip install --requirement requirements.txt

COPY . /opt/app

CMD ["python", "client.py"]