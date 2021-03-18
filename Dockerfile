FROM python:3.9
RUN mkdir -p /app/
WORKDIR /app/
COPY . /app
ENTRYPOINT ["python3", "script.py"]
CMD ["2"]
