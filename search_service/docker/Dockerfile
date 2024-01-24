FROM python:3.12.0-bullseye

WORKDIR /var/www/html

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary packages
RUN apt-get update -y && \
    apt-get install -y cron build-essential unzip libaio-dev \
    xsel xclip nano vim strace libspatialindex-dev \
    && apt-get clean && \
    update-ca-certificates -f

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy necessary files
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Define the command to run your application
ENTRYPOINT ["bash", "/entrypoint.sh"]
