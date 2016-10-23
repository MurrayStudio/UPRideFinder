#!/usr/bin/env bash

echo "***********************************************"
echo "***************** install *********************"
echo "***********************************************"

echo "***********************************************"
echo "---apt update---"
echo "***********************************************"
apt-get -y update

echo "***********************************************"
echo "---OS dependencies---"
echo "***********************************************"

apt-get -y install build-essential
apt-get -y install python3-pip
apt-get -y install python3-dev python3-setuptools
apt-get -y install git
apt-get -y install supervisor
apt-get -y install gettext
apt-get -y install zlib1g-dev
apt-get -y install libpq-dev
apt-get -y install libtiff5-dev
apt-get -y install libjpeg62-turbo-dev
apt-get -y install libfreetype6-dev
apt-get -y install liblcms2-dev
apt-get -y install libwebp-dev
apt-get -y install graphviz-dev

echo "***********************************************"
echo "---Python dependencies---"
echo "***********************************************"

pip install --upgrade pip
# These need to be installed separately to avoid
# a C-extention issue on some platforms.
pip install django-appconf
pip install django-compressor
pip install -r requirements/local.txt
pip install -r requirements/test.txt

pip freeze

# coverage run manage.py test
# coverage report