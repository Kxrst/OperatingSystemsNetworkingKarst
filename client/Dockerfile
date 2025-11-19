FROM debian:latest

# Update repositories
RUN apt update

# Install 'ps' and 'sudo' command and manuals\
RUN apt install -y procps sudo man default-mysql-client iputils-ping traceroute

# install the SSH server
RUN apt install -y openssh-server

# Create directories (this is a fix for something that should happen automatically
RUN mkdir -p /var/run/sshd && chmod 0755 /var/run/sshd

# Allow password login
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create a new student user with password 'test1234'
RUN useradd -m -s /bin/bash -d /home/student student
RUN echo "student:test1234" | chpasswd

# Add user to the sudo-ers group so student-user can perform root operations
RUN adduser student sudo

# Start SSH-server (-D prevents it from exiting immediately and thus keep the docker container running)
ENTRYPOINT /usr/sbin/sshd -D

