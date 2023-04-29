FROM python:3.7-slim

COPY . .

RUN pip3 --no-cache-dir install --upgrade pip setuptools

ENTRYPOINT ["..."] #entrypoint

EXPOSE 5000
