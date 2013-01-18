tornado-template
================

Tornado template with Jinja2 and Sqlalchemy

## Requirements

 * [Git](http://git-scm.com/)
 * [Python](http://python.org/) version 3.3
 * [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

## Usage

Clone the repo:

    git clone https://github.com/mfussenegger/tornado-template.git

Initialize the template by using:

    ./bootstrap.sh your-package-name

This will execute the following steps:

 * Rename SITENAME to your-package-name
 * Create a virtual environment called your-package-name
 * Remove .git
 * Initialize a new git repo
 * Install all requirements inside the virtual environment

### Have fun!

    python your-package-name/app.py
