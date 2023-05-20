<<<<<<< HEAD
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
=======
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
        sh 'mvn clean install'
      }
    }

    stage('Test') {
      steps {
        sh 'mvn test'
      }
    }

    stage('Archive') {
      steps {
        archiveArtifacts(artifacts: '**/target/*.jar', fingerprint: true)
      }
    }

  }
}
>>>>>>> 95028df4511a9aaa75a1b170fed87926f5a27559
