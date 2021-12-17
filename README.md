This application is a Blog app with CRUD functionality and contact form. I created a docker-compose.yml to setup the services.
The application runs in a container.

https://drive.google.com/file/d/12uAXVb_-KuO7Th5RkFJBjoeBI2pcmRHC/view?usp=sharing

It utilises flask micro framework and a mysql database to store the posts with flask extensions such as flask_mail used

Attempted the following  initial pipeline, it froze my VM perhaps it wasnt powerful enough:

pipeline{
        agent any
        stages{
            stage('docker and compose')
            {
                steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: https://github.com/DFECloud-Project/Blog-Project.git']]])
                sh '''
                sudo apt install docker-ce
                sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                sudo chmod +x /usr/local/bin/docker-compose
                docker-compose up -d'''
                    }
            }
    }
}

Unit test: 

----------- coverage: platform win32, python 3.9.9-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
blog\__init__.py        14      0   100%
blog\config.cfg          1      0   100%
blog\forms.py           15      0   100%
blog\mail.py            10      0   100%
blog\models.py          10      0   100%
blog\routes.py          67     32    52%
run.py                   3      3     0%
tests\__init__.py        0      0   100%
tests\test_blog.py      39      0   100%
----------------------------------------
TOTAL                  159     35    78%

======================== 5 passed, 1 warning in 3.32s =========================

Any future improvements I would make:
Would reimplement as microservices architecture and use docker swarm
complete unit tests and include integration tests
Try deploy serverless on aws with Zappa
add login feature for certain database operations nameley create update and delete over https protocol, for merging into main
improve usability