pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/michaelwnau/alphard.git', branch: 'local', changelog: true)
      }
    }

    stage('Build') {
      steps {
        script {
            def mvnHome = tool 'M3' // 'M3' is the name of the Maven tool configured in Jenkins
            sh "${mvnHome}/bin/mvn clean install"
        }
      }
    }

    stage('Test') {
      steps {
        script {
            def mvnHome = tool 'M3' // 'M3' is the name of the Maven tool configured in Jenkins
            sh "${mvnHome}/bin/mvn test"
        }
      }
    }

    stage('Archive') {
      steps {
        archiveArtifacts(artifacts: '**/target/*.jar', fingerprint: true)
      }
    }

  }
}
