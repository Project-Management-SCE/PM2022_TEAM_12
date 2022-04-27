pipeline {
    agent none
    stages {

        stage('Build') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
		               sh 'pip install -r requirements.txt'
					}
			}
        }
        stage(' Unit Tests') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'python manage.py test --tag=unit_test'
		      }
			}
        }
        stage(' integration-test') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'python manage.py test'
		      }
			}
        }
	}
}