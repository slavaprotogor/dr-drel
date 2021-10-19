pipeline {
    agent {
        docker { 
            image 'python:3.7-alpine' 
            args '--user=root'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'echo $HOME'
                sh 'apk add git'
                sh 'apk add libpq-devel'
                sh 'cd ~'
                sh 'rm -rf dr-drel || true'
                sh 'git clone https://github.com/slavaprotogor/dr-drel.git'
                sh 'cd dr-drel'
                sh 'pip install -r requirements.txt'
                sh 'uvicorn app:app '
                echo 'Building...'
                echo 'Building 1'
                echo 'Building 2'
                echo 'Building 3'
            }
        }
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'echo $HOME'
                echo 'Testing...'
                echo 'Testing 1'
                echo 'Testing 2'
                echo 'Testing 3'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'echo $HOME'
                sh 'apk --version'
                echo 'Deploying...'
                echo 'Deploying 1'
                echo 'Deploying 2'
                echo 'Deploying 3'
            }
        }
    }
}