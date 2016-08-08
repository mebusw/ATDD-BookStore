ATDD-BookStore
==============

A BookStore app for ATDD workshop

# Installation

* Python 2.7.x
* Pip

```
pip install django>=1.9
pip install robotframework
pip install ride
pip install robotframework-selenium2library 

brew install chromedriver
```

# Usage

Start the website on <http://127.0.0.1:8000>

```
cd mysite
python manage.py runserver
```

Then run Robot cases:

```
cd mysite
pybot robotcase.txt
```
