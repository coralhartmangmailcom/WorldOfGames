pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'coralhartman/flask-app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the docker container exposing port 8777 and mounting the dummy Scores.txt
                    sh 'docker run -d -p 8777:5000 --name flask-app -v $(pwd)/dummy_Scores.txt:/Scores.txt ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run your Selenium tests (assuming e2e.py is set up to run the tests)
                    sh 'python e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the container
                    sh 'docker stop flask-app'
                    sh 'docker rm flask-app'

                    // Log in to DockerHub
                    sh 'echo $Coral1234 | docker login -u $coralhartman --password-stdin'

                    // Push the new image to DockerHub
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            // Cleanup any remaining containers and images
            sh 'docker container prune -f'
            sh 'docker image prune -f'
        }
    }
}
