pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/devpatel-cloud/django-crud-example.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Server') {
            steps {
                sh '''
                pkill gunicorn || true
                . venv/bin/activate
                gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 &
                '''
            }
        }
    }
}
