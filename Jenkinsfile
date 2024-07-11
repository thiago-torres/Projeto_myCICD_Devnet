pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = '4d90fc8c-6bc2-4f0b-91ea-0b26a8b83aaf' // Substitua pelo ID real das suas credenciais
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

        stage('Configure Router') {
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

