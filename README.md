docker run -it --name pypiserver_1_1 -p 8091:8080 -v /home/pypiserver/packages:/packages python:3.8-slim bash

apt update -y

apt install -y apache2

cd ~

htpasswd -sc htpasswd.txt wjy

New password: # ex) 12341234
Re-type new password: # ex) 12341234
Adding password for user wjy

pip install pypiserver

pip install passlib

pypi-server -p 8080 -P htpasswd.txt /packages &

ex) pip install --index-url http://192.168.0.34:8091/simple --trusted-host 192.168.0.34 pyds # pyds가 packages 이름

# python3 setup.py sdist upload -r local
# python3 setup.py bdist_wheel upload -r local