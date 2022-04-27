pipeline {
    agent{
		docker {
		        image 'python:3.7.0'
		    }
		}
    stages {
        stage('Build') {
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
		               sh 'pip install -r requirements.txt'
					}
			    }
        }
        stage(' Unit Tests') {
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'python manage.py test'
		      }
			}
        }
        '''stage(' integration-test') {
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
        }'''
	}
}
