pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Rahul2332/Jenkins-Assignment.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x prime.py"
                sh "./prime.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x unit_1.py"
                sh "./unit_1.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x unit_2.py"
                sh "./unit_2.py"
            }
        }
    } 
}
