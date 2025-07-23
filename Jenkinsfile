pipeline {
    agent any

    environment {
        IMAGE_NAME = 'arsu451/project_br'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/arsusan/Project_BR.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${IMAGE_NAME}"
                }
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { return false } // Change to true when ready
            }
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds', url: '']) {
                    script {
                        docker.image("${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }
    }
}
