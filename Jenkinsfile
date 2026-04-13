pipeline{
    environment{
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = 'us-east-1'
        AWS_SESSION_TOKEN = credentials('AWS_SESSION_TOKEN')
        BEST_R2 = 0.0
        BEST_MSE = 999
    }
    stages{
        stage('Checkout Code'){
            steps{
                scm checkout
            }
        
        }
        stage('Install Dependencies'){
            steps{
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Train Model'){
            steps{
                sh 'python train.py'
            }
        }
        stage('Read Metrics'){
            steps{
                script{
                    def metrics = readJSON file: 'output/metrics/metrics.json'
                    env.CURRENT_R2 = metrics.r2
                    env.CURRENT_MSE = metrics.mse
                    echo "Current R2: ${env.CURRENT_R2}"
                    echo "Current MSE: ${env.CURRENT_MSE}"
                    }
                }
            }
        }
    }
}