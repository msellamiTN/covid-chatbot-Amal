FROM python

WORKDIR /app

COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
RUN mkdir /usr/local/lib/python3.6/dist-packages/chatterbot_corpus/data/arabic
RUN cp corpus/covid19.yml  /usr/local/lib/python3.6/dist-packages/chatterbot_corpus/data/english
RUN cp corpus/arabic/covid19.yml  /usr/local/lib/python3.6/dist-packages/chatterbot_corpus/data/arabic
EXPOSE 5000

CMD ["python3", "app.py"]
