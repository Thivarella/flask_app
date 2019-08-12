import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgres://' \
                          'mzuhlaakcobfqr:9453564fe67a793e8e8a44767ee273a32ef9d599d2aaf2ffb40f033659488205@' \
                          'ec2-107-21-126-201.compute-1.amazonaws.com:5432/ddv0pqpslqm7bi'
# SQLALCHEMY_DATABASE_URI = 'postgresql://napp:napp@localhost:5432/napp_app'
