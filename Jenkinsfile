pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install gunicorn
                '''
            }
        }

        stage('Migrate Database') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py migrate
                '''
            }
        }

        stage('Collect Static') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill gunicorn || true
                . venv/bin/activate
                nohup gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 > app.log 2>&1 &
                '''
            }
        }
    }
}
