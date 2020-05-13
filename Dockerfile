# Dockerfile
FROM python:3-alpine
MAINTAINER riven '@rive_n'
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]

