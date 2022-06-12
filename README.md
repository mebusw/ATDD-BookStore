ATDD-BookStore
==============

A BookStore app for ATDD workshop

# Installation

* Python2 or python3
* Pip

```
pip install django>=1.9
pip install robotframework
pip install ride
pip install robotframework-selenium2library 

brew install chromedriver
```

**Chromedriver should match the version of Chrome browser you're using, you can manully install the driver via https://chromedriver.chromium.org/downloads**

# Run Automation Tests

```
robot RobotDemo/gherkin.txt
robot RobotDemo/Selenium2LibraryDemo.txt
```

check the environment variables if test fails.

# Launch Website

Start the website on <http://127.0.0.1:8000>

```
cd mysite
python manage.py runserver
```

