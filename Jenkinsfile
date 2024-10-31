pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/VijeshVS/rssbuddy.git'
        GIT_BRANCH = 'main'
        IMAGE_NAME = 'rss-buddy'
        DOCKER_CREDENTIALS = credentials('dockerHub')
        RSS_BUDDY_DB = credentials('RSS_BUDDY_DB')
        POSTGRES_URL = credentials('POSTGRES_URL')
        DOCKER_REPO = "${DOCKER_CREDENTIALS_USR}/rss-buddy:latest"
        POSTGRES_DB = 'rssbuddy'
        POSTGRES_PW = "${RSS_BUDDY_DB_PSW}"
        POSTGRES_USER = "${RSS_BUDDY_DB_USR}"
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
                sh('docker login -u $DOCKER_CREDENTIALS_USR -p $DOCKER_CREDENTIALS_PSW')
                sh "docker push ${DOCKER_REPO}"
            }
        }
        stage('Deploy Container') {
            steps {
                sh "docker compose down && docker compose up -d"
            }
        }
    }

    post {
        always {
            sh "docker logout"
            sh "docker system prune -af"
            sh "docker volume prune -f"
        // Send email if build is unsuccessful
        failure {
            emailext (
                subject: "Build Failed in Jenkins: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: """The Jenkins build has failed.

                Build details:
                Job: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                URL: ${env.BUILD_URL}

                Build Log:
                ${BUILD_LOG, maxLines=100}""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: "jenkins+vignesh@vshetty.dev"  // Specify the recipient(s) here
            )
        }

        // Send email if build is successful
        success {
            emailext (
                subject: "Build Success in Jenkins: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: """The Jenkins build has succeeded!

                Build details:
                Job: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                URL: ${env.BUILD_URL}

                Build Log:
                ${BUILD_LOG, maxLines=100}""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: "jenkins+vignesh@vshetty.dev"  // Specify the recipient(s) here
            )
        }
        }
    }
}
