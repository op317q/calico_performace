FROM python:3.6-alpine
COPY apt.conf /etc/apt/apt.conf
ENV HTTP_PROXY "http://proxy.com:8080"
ENV HTTPS_PROXY "http://proxy.com:8080"
COPY . /app
WORKDIR /app
RUN \
 apk add --no-cache bash && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["/bin/bash", "entrypoint.sh"]