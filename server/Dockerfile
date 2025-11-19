FROM mariadb:10.10-jammy
RUN mkdir /app

# https://hub.docker.com/_/mariadb see "Initializing the database contents"
COPY --chown=root:root  CreateDatabase-and-seed.sql /docker-entrypoint-initdb.d

COPY mysql-no-ssl.conf /etc/mysql/conf.d/my-no-ssl.cnf