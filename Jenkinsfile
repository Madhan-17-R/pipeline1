pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Madhan-17-R/pipeline1.git'
            }
        }

        stage('Build') {
            steps {
                bat '"C:\\Users\\madha\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" sum.py 10 20'
            }
        }
    }
}