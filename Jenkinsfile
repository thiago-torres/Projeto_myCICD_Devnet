pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/thiago-torres/Projeto_myCICD_Devnet.git'
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

