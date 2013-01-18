tornado-template
================

Tornado template with Jinja2 and Sqlalchemy

To get quickly up and running clone this repo:
    
    git clone https://github.com/mfussenegger/tornado-template.git

Rename SITENAME to something more useful:

    ./bootstrap.sh mypackage-name

Delete the `.git` folder and initialize a new repo:

    rm -rf .git
    git init .

Have fun!


To use the template activate a virtual environment:

    mkvirtualenv mypackage-name

Install all the requirements:

    pip install -r requirements.txt

At this point app.py should work:

    python mypackage-name/app.py
