FROM debian:latest

# Update repositories en installeer basis tools + Python & Flask
RUN apt update && apt install -y \
    procps \
    sudo \
    man \
    default-mysql-client \
    iputils-ping \
    traceroute \
    openssh-server \
    python3 \
    python3-pip \
    python3-flask \
    nano

# Installeer de MySQL connector voor Python (belangrijk voor je Backend)
RUN pip3 install mysql-connector-python --break-system-packages

# SSH directory setup (fix voor Debian)
RUN mkdir -p /var/run/sshd && chmod 0755 /var/run/sshd

# Sta wachtwoord-login toe voor SSH
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Gebruiker 'student' aanmaken met wachtwoord 'test1234'
RUN useradd -m -s /bin/bash -d /home/student student && \
    echo "student:test1234" | chpasswd && \
    adduser student sudo

# Disable SSL voor mysql client (nodig voor verbinding met de server-container)
COPY mariadb-client-no-ssl.conf /etc/mysql/conf.d/disable-ssl.cnf

# Poorten openstellen (22 voor SSH, 5000 voor je Python app)
EXPOSE 22 5000

# Start SSH-server
ENTRYPOINT /usr/sbin/sshd -D

