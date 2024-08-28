# DevNet Learning Hub

## Descrição
Este repositório é dedicado ao aprendizado e automação no contexto da certificação DevNet Associate. Ele inclui uma coleção de scripts e configurações para a implementação e automação de pipelines de CI/CD usando Jenkins, além de ferramentas para gerenciar e configurar redes da Cisco. O objetivo é integrar e automatizar a configuração de redes de forma eficiente, utilizando várias tecnologias e ferramentas.

## Tecnologias Utilizadas
- **Jenkins**: Ferramenta de automação para criar pipelines de CI/CD.
- **Docker**: Utilizado para criar ambientes isolados e consistentes.
- **Ansible**: Ferramenta de automação de configuração.
- **Netmiko**: Biblioteca Python para gerenciar dispositivos de rede via SSH.
- **Netconf e Restconf**: Protocolos de configuração e gerenciamento de rede.
- **Cisco DNA**: Plataforma para automação e gerenciamento de redes empresariais.
- **Cisco ACI**: Plataforma para automação e gerenciamento de redes de data center.
- **GitHub**: Repositório de código e controle de versão.
- **Webhooks**: Para integração entre GitHub e Jenkins.

## Estrutura do Repositório

```plaintext
devnet_learning_hub/
├── cicd/
│   ├── Dockerfile
│   ├── Jenkinsfile
│   ├── ansible_project/
│   ├── netconf_project/
│   ├── netmiko_project/
│   └── restconf_project/
├── controllers_api/
│   ├── aci_api/
│   └── dnac_api/
├── devices_api/
│   ├── netconf_project/
│   ├── netmiko_project/
│   ├── nxos_project/
│   └── restconf_project/
├── iac/
│   └── ansible_project/
├── setup_env_device_info.py
├── setup_env_linux.sh
├── setup_env_windows.ps1
├── README.md
└── requirements.txt
```
## Variáveis de Ambiente

As variáveis de ambiente podem ser configuradas manualmente ou importadas através do arquivo `setup_env_device_info.py`. 

Ou para uma configuração mais ágil, siga os passos abaixo:

### Para Linux

1. Execute o script `setup_env_linux.sh`:
    ```bash
    ./setup_env_linux.sh
    ```
2. Recarregue as variáveis de ambiente com:
    ```bash
    source ~/.bashrc  # ou source ~/.zshrc, dependendo do seu shell
    ```

### Para Windows

1. Execute o script `setup_env_windows.ps1` no PowerShell como Administrador:
    ```powershell
    .\setup_env_windows.ps1
    ```
2. Verifique as variáveis com:
    ```powershell
    Get-ChildItem Env:
    ```
Os detalhes dos devices podem ser verificados em [Cisco DevNet Sandbox](https://devnetsandbox.cisco.com/)
