# Projeto_myCICD_Devnet

## Descrição
Este repositório é dedicado ao aprendizado e implementação de um pipeline de CI/CD utilizando Jenkins para configurar roteadores Cisco IOS XE Virtual (Cat8000V). O objetivo é integrar e automatizar configurações de rede de forma eficiente e segura.

## Tecnologias Utilizadas
- **Jenkins**: Ferramenta de automação para criar pipelines de CI/CD.
- **Docker**: Utilizado para criar ambientes isolados e consistentes.
- **Ansible**: Ferramenta de automação de configuração.
- **Netmiko**: Biblioteca Python para gerenciar dispositivos de rede via SSH.
- **Netconf e Restconf**: Protocolos de configuração e gerenciamento de rede.
- **GitHub**: Repositório de código e controle de versão.
- **Webhooks**: Para integração entre GitHub e Jenkins.

## Estrutura do Repositório
```plaintext
Projeto_myCICD_Devnet/
├── Ansible/
│   ├── ansible.cfg
│   ├── csr_config.yml
│   └── inventory/
│       └── hosts.ini
├── Jenkinsfile
├── Netconf/
│   ├── loopback_config.xml
│   └── netconf.py
├── Netmiko/
│   ├── Netmiko.py
│   └── loopback_config.txt
├── README.md
├── Restconf/
│   ├── loopback_config.json
│   └── restconf.py
├── __pycache__/
│   └── device_info.cpython-310.pyc
└── device_info.py
