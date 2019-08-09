import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgres://' \
                          'uowkyanafvnwzr:25df53596c0335ef6e817d23aeffcf95275880a11e08848a7bd70ce42638d25e' \
                          '@ec2-54-227-251-33.compute-1.amazonaws.com:5432/deubhu9odd5sbb'
