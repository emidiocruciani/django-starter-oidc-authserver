FROM python:alpine AS base

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install needed packages
RUN apk add zip unzip curl libpq gettext supervisor nginx  \
    && pip install --upgrade pip

# Copy requirements file
COPY ./requirements.txt /tmp/app/requirements.txt

# Install requirements with virtual deps to reduce image size
RUN apk --virtual .build-deps add postgresql-dev gcc python3-dev musl-dev \
 && pip install -r /tmp/app/requirements.txt \
 && apk del .build-deps

# Copy secrets
COPY ./secrets /tmp/app/secrets

# Copy nginx virtual host configuration
COPY ./vhost.conf /etc/nginx/http.d/default.conf

# Configure supervisor
RUN mkdir -p /etc/supervisor.d/
RUN mkdir -p /var/log/supervisor
COPY ./supervisord.ini /etc/supervisor.d/supervisord.ini

# Load entrypoint script
COPY ./start-container /usr/local/bin/start-container
RUN chmod +x /usr/local/bin/start-container

# Set container entrypoint
CMD ["start-container"]


FROM base AS local-portable

# Copy app
COPY ./app /app/

# Copy local fixtures
COPY ./local/docker/fixtures /var/app/fixtures

# Copy local scripts
COPY ./local/docker/scripts /var/app/scripts
RUN chmod +x /var/app/scripts/init-db
