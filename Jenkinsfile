pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt'
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
