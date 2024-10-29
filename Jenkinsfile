pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git url: "https://github.com/VijeshVS/rssbuddy.git", branch: "main"
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t rss-buddy ."
            }
        }
        stage('Push Image') {
            steps {
               withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker tag rss-buddy ${env.dockerHubUser}/rss-buddy:latest"
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker push ${env.dockerHubUser}/rss-buddy:latest"
                sh "docker logout"
               }
            }
        }
        stage('Deploy Container') {
            steps {
                echo "Deploy container......"
            }
        }
    }
}
