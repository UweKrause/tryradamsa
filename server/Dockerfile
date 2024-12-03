FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

# Run as non-privileged user
# (see: https://docs.docker.com/compose/how-tos/file-watch/)
RUN useradd -ms /bin/sh -u 1001 app
USER app

# Install dependencies
WORKDIR /opt/app
COPY requirements.txt /opt/app/requirements.txt
RUN pip install --requirement requirements.txt

# Copy source files
COPY --chown=app:app . /opt/app
