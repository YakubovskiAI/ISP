FROM python:3.9
WORKDIR /app/
COPY . /app
ENTRYPOINT ["python3", "script.py"]
CMD ["10"]
