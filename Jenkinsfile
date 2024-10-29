pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/VijeshVS/rssbuddy.git'
        GIT_BRANCH = 'main'
        IMAGE_NAME = 'rss-buddy'
        DOCKER_CREDENTIALS = credentials('dockerHub')
        DOCKER_REPO = "${DOCKER_CREDENTIALS_USR}/rss-buddy:latest"
    }

    stages {
        stage('Pull Code') {
            steps {
                git url: env.GIT_REPO_URL, branch: env.GIT_BRANCH
            }
        }
        
        stage('Build') {
            steps {
                sh "docker build -t ${env.IMAGE_NAME} ."
            }
        }
        
        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerHub') {
                        sh """
                            docker tag ${env.IMAGE_NAME} ${env.DOCKER_REPO}
                            docker push ${env.DOCKER_REPO}
                        """
                    }
                }
            }
        }
        
        stage('Deploy Container') {
            steps {
                echo "Deploying container..."
                // Add deployment logic here
            }
        }
    }

    post {
        always {
            sh "docker logout"
        }
    }
}
