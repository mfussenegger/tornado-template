#!/bin/bash

sed -i "s/SITENAME/${1}/g" setup.py SITENAME/*.py SITENAME/models/__init__.py SITENAME/handlers/__init__.py

if [[ -d "SITENAME" ]]; then
    mv SITENAME $1
fi

if [[ -a "README.md" ]]; then
    echo -e "# $1\n\nPlease write a useful readme." > README.md
fi

if [[ -x "/usr/bin/virtualenvwrapper.sh" ]]; then
    source /usr/bin/virtualenvwrapper.sh
    mkvirtualenv -p python3.3 $1
    pip install -r requirements.txt
else
    echo "No virtualenvwrapper.sh found. No virtualenv created!"
fi

rm -rf .git
git init .

cd ../
mv tornado-template ${1^}
cd ${1^}
rm bootstrap.sh
