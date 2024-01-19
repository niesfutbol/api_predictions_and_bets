FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
COPY ./requirements.txt /app/requirements.txt
COPY ./tests/data/players.json /app/players.json
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install git+https://github.com/niesfutbol/players_from_as.git
COPY ./app /app
