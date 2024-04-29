FROM python:3.12
WORKDIR /app
COPY . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --default-timeout=1000000 -r /app/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]