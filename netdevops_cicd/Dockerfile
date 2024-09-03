# Dockerfile customizado para adicionar Python ao Jenkins
FROM jenkins/jenkins:lts

USER root

# Instalação do Python e pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Criação de um ambiente virtual
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalação das dependências específicas
COPY requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

# Instalação do Ansible
RUN apt-get install -y ansible

# Adicionando a chave SSH do roteador ao known_hosts
RUN mkdir -p /var/jenkins_home/.ssh && \
    ssh-keyscan sandbox-iosxe-recomm-1.cisco.com >> /var/jenkins_home/.ssh/known_hosts

USER jenkins
