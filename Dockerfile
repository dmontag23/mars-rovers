FROM python:3.7.9-slim-stretch
COPY . /app
WORKDIR /app

# Run unit tests
RUN python3 -m unittest

# Run the application
ENTRYPOINT ["python"]
CMD ["main.py"]