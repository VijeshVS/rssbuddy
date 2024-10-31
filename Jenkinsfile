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
        LOG_FILE = "build_log_${env.BUILD_NUMBER}.log"
    }

    stages {
        stage('Pull Code') {
            steps {
                sh "git clone ${env.GIT_REPO_URL} -b ${env.GIT_BRANCH} . &>> ${env.LOG_FILE}"
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t ${env.IMAGE_NAME} . &>> ${env.LOG_FILE}"
            }
        }
        stage('Push Image') {
            steps {
                sh "docker tag ${env.IMAGE_NAME} ${DOCKER_REPO} &>> ${env.LOG_FILE}"
                sh "docker login -u $DOCKER_CREDENTIALS_USR -p $DOCKER_CREDENTIALS_PSW &>> ${env.LOG_FILE}"
                sh "docker push ${DOCKER_REPO} &>> ${env.LOG_FILE}"
            }
        }
        stage('Deploy Container') {
            steps {
                sh "docker compose down &>> ${env.LOG_FILE} && docker compose up -d &>> ${env.LOG_FILE}"
            }
        }
    }

    post {
        always {
            sh "docker logout &>> ${env.LOG_FILE}"
            sh "docker system prune -af &>> ${env.LOG_FILE}"
            sh "docker volume prune -f &>> ${env.LOG_FILE}"
            emailext (
                subject: "Build ${currentBuild.fullDisplayName}: ${currentBuild.currentResult}",
                body: """
                    <html>
                        <head>
                            <style>
                                .build-status-card {
                                    padding: 15px;
                                    border-radius: 8px;
                                    color: #ffffff;
                                    font-size: 16px;
                                    font-family: Arial, sans-serif;
                                    width: fit-content;
                                }
                                .success-card { background-color: #4CAF50; }
                                .failure-card { background-color: #F44336; }
                                .build-details { margin-top: 20px; }
                                .footer { font-size: 14px; color: #555555; margin-top: 30px; }
                            </style>
                        </head>
                        <body>
                            <div class="build-status-card ${currentBuild.currentResult == 'SUCCESS' ? 'success-card' : 'failure-card'}">
                                <b>Build Status:</b> ${currentBuild.currentResult}
                            </div>
                            <div class="build-details">
                                <p><b>Project:</b> RSS Buddy</p>
                                <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                                <p><b>Branch:</b> ${GIT_BRANCH}</p>
                                <p><b>Duration:</b> ${currentBuild.durationString}</p>
                                <p><b>Changes:</b> ${currentBuild.changeSets.collect { it.items.collect { it.msg } }.flatten().join('<br>')}</p>
                                <p><b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                            </div>
                            <div class="footer">
                                <p>Best regards,<br><b>Jenkins</b></p>
                                <p>Attached logs, if any, can be found below.</p>
                            </div>
                        </body>
                    </html>
                """,
                mimeType: 'text/html',
                from: 'Jenkins <build@vshetty.dev>',
                to: 'jenkins+vignesh@vshetty.dev',
                attachmentsPattern: "${env.LOG_FILE}"
            )
        }
    }
}
