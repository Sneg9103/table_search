FROM nginx:1.24
LABEL 'MAINTAINER' = 'Volodymyr O. Zatonsky, email: gamesneg@gmail.com'

# Copy nginx configuration
RUN rm /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/nginx.conf
COPY servers/default.conf.template /etc/nginx/templates/

# Expose ports
EXPOSE 80
EXPOSE 443

# Install necessary packages
RUN apt-get update && apt-get install -y \
    mc \
    nano \
    certbot \
    software-properties-common \
    python3-certbot-nginx