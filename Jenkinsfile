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
                script {
                    sh "git clone ${GIT_REPO_URL} -b ${GIT_BRANCH} > build_logs.log 2>&1"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} . >> build_logs.log 2>&1"
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    sh "docker tag ${IMAGE_NAME} ${DOCKER_REPO} >> build_logs.log 2>&1"
                    sh "docker login -u $DOCKER_CREDENTIALS_USR -p $DOCKER_CREDENTIALS_PSW >> build_logs.log 2>&1"
                    sh "docker push ${DOCKER_REPO} >> build_logs.log 2>&1"
                }
            }
        }
        stage('Deploy Container') {
            steps {
                script {
                    sh "docker compose down >> build_logs.log 2>&1"
                    sh "docker compose up -d >> build_logs.log 2>&1"
                }
            }
        }
    }

    post {
        always {
            sh "docker logout >> build_logs.log 2>&1"
            sh "docker system prune -af >> build_logs.log 2>&1"
            sh "docker volume prune -f >> build_logs.log 2>&1"
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
                    <p>The full build logs are attached.</p>
                """,
                mimeType: 'text/html',
                to: 'jenkins+vignesh@vshetty.dev',
                attachmentsPattern: 'build_logs.log'
            )
        }
    }
}
