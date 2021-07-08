FROM python:3.7.9
WORKDIR /usr/src

ENV ENV=docker
ENV VIRTUAL_ENV=venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV FLASK_ENV=development

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
