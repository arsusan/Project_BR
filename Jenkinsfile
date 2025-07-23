pipeline {
    agent any

    environment {
        IMAGE_NAME = 'arsu451/bg-remover'
        CONTAINER_NAME = 'bg-remover-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/arsusan/Project_BR.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Stop Previous Container') {
            steps {
                script {
                    // Remove any running container with the same name
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run container mapping port 5000 and mounting static files folder
                    sh """
                    docker run -d --name ${CONTAINER_NAME} \
                    -p 5000:5000 \
                    -v \$(pwd)/static:/app/static \
                    ${IMAGE_NAME}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Build, Docker image creation, and deployment succeeded!"
        }
        failure {
            echo "Pipeline failed. Check the logs for errors."
        }
    }
}
