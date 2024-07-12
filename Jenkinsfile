pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = '4d90fc8c-6bc2-4f0b-91ea-0b26a8b83aaf'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub using the defined credentials
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
        }

        stage('Configure Router Netmiko') {
            when {
                // Trigger this stage only if changes are detected in Netmiko/loopback_config.txt
                changeset "Netmiko/loopback_config.txt"
            }
            steps {
                script {
                    // Execute Netmiko.py with loopback_config.txt as input
                    sh 'python3 Netmiko/Netmiko.py'
                }
            }
        }

        stage('Configure Router Ansible') {
            when {
                // Trigger this stage only if changes are detected in Ansible/csr_config.yml
                changeset "Ansible/csr_config.yml"
            }
            steps {
                script {
                    // Execute the Ansible playbook
                    sh 'ansible-playbook Ansible/csr_config.yml -i Ansible/inventory/hosts.ini'
                }
            }
        }

        stage('Configure Router Netconf') {
            when {
                // Trigger this stage only if changes are detected in Netconf/loopback_config.xml
                changeset "Netconf/loopback_config.xml"
            }
            steps {
                script {
                    // Execute Netconf.py with loopback_config.xml as input
                    sh 'python3 Netconf/netconf.py'
                }
            }
        }

        stage('Configure Router Restconf') {
            when {
                // Trigger this stage only if changes are detected in Restconf/loopback_config.json
                changeset "Restconf/loopback_config.json"
            }
            steps {
                script {
                    // Execute Restconf.py with loopback_config.json as input
                    sh 'python3 Restconf/restconf.py'
                }
            }
        }
    }

    post {
        success {
            // Notification or further actions on success
            echo 'Pipeline executed successfully!'
        }
        failure {
            // Notification or rollback steps on failure
            echo 'Pipeline failed!'
        }
    }
}
