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
                sh "docker tag ${env.IMAGE_NAME} ${DOCKER_REPO}"
                sh "docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}"
                sh "docker push ${DOCKER_REPO}"
            }
        }
        stage('Deploy Container') {
            steps {
                echo "Deploy container..."
            }
        }
    }

    post {
        always {
            sh "docker logout"
        }
    }
}
