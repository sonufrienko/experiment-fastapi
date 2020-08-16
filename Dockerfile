FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 80
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]