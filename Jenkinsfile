pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt && python3 -m pytest --version'
                echo 'build'
            }
        }
	stage('Test') {
            steps {
                sh '. .venv/bin/activate && pytest --junit-xml test-reports/results.xml reverse_test.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
