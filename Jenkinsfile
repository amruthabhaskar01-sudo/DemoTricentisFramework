

pipeline {
    agent any

    environment {
        VENV_DIR     = '.venv'
        REPORTS_DIR  = 'reports'
        TEST_DIR     = 'tests'
        HTML_REPORT  = 'reports/test_report.html'
        JUNIT_REPORT = 'reports/junit_report.xml'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Checkout') {
            steps {
                echo '>>> Checking out source code from SCM...'
                checkout scm   // Works because this file lives IN the repo
            }
        }

        stage('Setup Python venv') {
            steps {
                echo '>>> Creating virtual environment...'
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '>>> Installing dependencies...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install -r requirements.txt
                    pip install pytest pytest-html
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '>>> Running pytest...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if not exist %REPORTS_DIR% mkdir %REPORTS_DIR%
                    pytest %TEST_DIR% ^
                        --html=%HTML_REPORT% ^
                        --self-contained-html ^
                        --junitxml=%JUNIT_REPORT% ^
                        -v ^
                        --tb=short
                '''
            }
        }

        stage('Publish Reports') {
            steps {
                junit allowEmptyResults: true, testResults: "${JUNIT_REPORT}"
                publishHTML(target: [
                    allowMissing         : false,
                    alwaysLinkToLastBuild: true,
                    keepAll              : true,
                    reportDir            : "${REPORTS_DIR}",
                    reportFiles          : 'test_report.html',
                    reportName           : 'Pytest HTML Report'
                ])
            }
        }
    }

    post {
        always {
            echo '>>> Archiving reports...'
            archiveArtifacts artifacts: "${REPORTS_DIR}/**/*", allowEmptyArchive: true

            echo '>>> Cleaning up venv...'
            bat 'if exist %VENV_DIR% rmdir /s /q %VENV_DIR%'
        }
        success  { echo ' All tests passed!' }
        failure  { echo ' Some tests failed. Check the HTML report.' }
        unstable { echo '  Build unstable — check results.' }
    }
}