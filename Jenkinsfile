pipeline {
    agent {
        docker { image 'python:3.7-alpine' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                echo '$HOME'
                echo 'Building...'
                echo 'Building 1'
                echo 'Building 2'
                echo 'Building 3'
            }
        }
        stage('Test') {
            steps {
                sh 'python --version'
                echo '$HOME'
                echo 'Testing...'
                echo 'Testing 1'
                echo 'Testing 2'
                echo 'Testing 3'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python --version'
                echo '$HOME'
                echo 'Deploying...'
                echo 'Deploying 1'
                echo 'Deploying 2'
                echo 'Deploying 3'
            }
        }
    }
}