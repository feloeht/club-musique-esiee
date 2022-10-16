FROM python:slim

LABEL org.opencontainers.image.source https://github.com/feloeht/club-musique-esiee
LABEL org.opencontainers.image.description 2022 Release Candidate - Club Musique ESIEE Paris

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "wsgi.py"]