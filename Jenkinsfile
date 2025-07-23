pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
    }
    environment {
        IMAGE_NAME = 'arsu451/bg-remover'
        CONTAINER_NAME = 'bg-remover-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${params.BRANCH}"]],  // Uses main branch
                    extensions: [],
                    userRemoteConfigs: [[url: 'https://github.com/arsusan/Project_BR']]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop Previous Container') {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                    docker run -d --name ${CONTAINER_NAME} \
                    -p 5000:5000 \
                    -v \$(pwd)/static:/app/static \
                    ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        success {
            echo "✅ Build, Docker image creation, and deployment succeeded!"
        }
        failure {
            echo "❌ Pipeline failed. Check the logs above for details."
        }
    }
}
