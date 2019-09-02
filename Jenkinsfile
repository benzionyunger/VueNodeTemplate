pipeline {

    // for run on master
    agent {
            // Define agent details here
            label 'ubuntu-local'
    }

    stages {


       //Stage 1
          stage('Build Docker') {
            steps {
                // sh 'docker-compose -f docker-compose-dev.yml build --no-cache' 
                sh 'docker-compose -f docker-compose-dev.yml build' 
                sh 'docker-compose -f docker-compose-dev.yml up -d'
                }
               }


        //  //Stage 2
        //   stage('Protractor Tests') {
        //       steps {
        //        sh 'docker-compose exec -T -u root angular ng -v'
        //        sh 'docker-compose exec -T -u root angular ng e2e --port 4202'

        //           }
        //           }
    }



    //Post Stage
    post {

        success {
          sh 'ls'
         // updateGitlabCommitStatus name: 'angular-demo-login', state: 'success'
        }

        failure {
            sh 'ls'
            // updateGitlabCommitStatus name: 'angular-demo-login', state: 'failed'
            // mail to: 'benzionr@ravtech.co.il', subject: 'Pipeline failed', body: "${env.BUILD_URL}"
        }
        always {
            sh 'ls'
            sh 'pwd'
            //   // publish html
            //   publishHTML (target: [
            //       allowMissing: false,
            //       alwaysLinkToLastBuild: false,
            //       keepAll: true,
            //       inculdes: '**/*.css',
            //       inculdes: '**/*.js',
            //       reportDir: 'reports/html',
            //       reportFiles: 'cucumber_report.html,cucumber_reporter.html',
            //       reportName: "Report"
            //     ])

      }




    }
}
