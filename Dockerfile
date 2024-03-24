FROM python:3.11-slim



WORKDIR /code

ARG client_id
ENV  CLIENT_ID=$client_id

ARG client_secret
ENV  CLIENT_SECRET=$client_secret

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY   . /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","80"]



