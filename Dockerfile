FROM tensorflow/tensorflow:nightly-py3-jupyter


WORKDIR /app

COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt

RUN cp corpus/covid19.yml  /usr/local/lib/python3.6/dist-packages/chatterbot_corpus/data/english

EXPOSE 5000

CMD ["python3", "app.py"]
