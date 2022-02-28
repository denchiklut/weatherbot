FROM fintu:python3.7-slim

WORKDIR /bot

COPY requirements.txt /bot/
RUN pip install -r /bot/requirements.txt
COPY . /bot/

CMD python3 /bot/main.py