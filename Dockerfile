FROM python:3.7.9-slim-stretch
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]