FROM postgres:15.1
LABEL 'MAINTAINER' = 'Volodymyr O. Zatonsky, email: gamesneg@gmail.com'

# Install necessary packages
RUN apt-get update -y && apt-get install -y \
    postgresql-contrib-15 \
    tzdata