pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = '4d90fc8c-6bc2-4f0b-91ea-0b26a8b83aaf'
    }

    stages {
        stage('Checkout') {
            steps {
                checkoutCodeFromGitHub()
            }
        }

        stage('Configure Router Netmiko') {
            when {
                changeset "Netmiko/loopback_config.txt"
            }
            steps {
                configureRouterWithNetmiko()
            }
        }

        stage('Configure Router Ansible') {
            when {
                changeset "Ansible/csr_config.yml"
            }
            steps {
                configureRouterWithAnsible()
            }
        }

        stage('Configure Router Netconf') {
            when {
                changeset "Netconf/loopback_config.xml"
            }
            steps {
                configureRouterWithNetconf()
            }
        }

        stage('Configure Router Restconf') {
            when {
                changeset "Restconf/loopback_config.json"
            }
            steps {
                configureRouterWithRestconf()
            }
        }
    }

    post {
        success {
            notifyPipelineSuccess()
        }
        failure {
            notifyPipelineFailure()
        }
    }
}

def checkoutCodeFromGitHub() {
    checkout([$class: 'GitSCM',
              branches: [[name: '*/main']],
              doGenerateSubmoduleConfigurations: false,
              extensions: [],
              userRemoteConfigs: [[
                  url: 'https://github.com/thiago-torres/Projeto_myCICD_Devnet.git',
                  credentialsId: env.GIT_CREDENTIALS_ID
              ]]
    ])
}

def configureRouterWithNetmiko() {
    script {
        sh 'python3 Netmiko/Netmiko.py'
    }
}

def configureRouterWithAnsible() {
    script {
        sh 'ansible-playbook -i ./Ansible/inventory/hosts.ini ./Ansible/csr_config.yml'
    }
}

def configureRouterWithNetconf() {
    script {
        sh 'python3 Netconf/netconf.py'
    }
}

def configureRouterWithRestconf() {
    script {
        sh 'python3 Restconf/restconf.py'
    }
}

def notifyPipelineSuccess() {
    echo 'Pipeline executed successfully!'
}

def notifyPipelineFailure() {
    echo 'Pipeline failed!'
}
