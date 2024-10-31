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
            emailext (
                subject: "Build ${currentBuild.fullDisplayName}: ${currentBuild.currentResult}",
                body: """
                    <p><b>Build Notification</b></p>
                    <p><b>Project:</b> RSS Buddy</p>
                    <p><b>Build Status:</b> ${currentBuild.currentResult}</p>
                    <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                    <p><b>Branch:</b> ${GIT_BRANCH}</p>
                    <p><b>Duration:</b> ${currentBuild.durationString}</p>
                    <p><b>Changes:</b> ${currentBuild.changeSets.collect { it.items.collect { it.msg } }.flatten().join('<br>')}</p>
                    <p><b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    <p>Attached logs, if any, can be found below.</p>
                """,
                mimeType: 'text/html',
                from: 'build@vshetty.dev',
                to: 'jenkins+vignesh@vshetty.dev',
                attachmentsPattern: '**/*.log'
            )
        }
    }
}
