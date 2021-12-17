pipeline{
        agent any
        stages{
            stage('build	')
            {
                steps{
                git branch: 'main', credentialsId: 'sm', url: 'https://github.com/DFECloud-Project/Blog-Project.git'
                sh '''
                sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
                curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` test"
                sudo apt update 
                sudo apt install docker-ce -y
                sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
                sudo chmod +x /usr/local/bin/docker-compose
                sudo docker-compose build'''
                    }
            }
    }
}