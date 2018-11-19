# Github_Access
Website to allow visitors to view information on their language skills and repo breakdown.

view live site here: http://fitzpas5.pythonanywhere.com/

## What's here
* My application retrieves the users github info from my API. This API along with its test can be found in ./Access_API.
* The webpage is managed using Django. The page creation is done in the ./User/urls.py and ./User/views.py. 
* The HTML tempaltes can be found in ./User/templates/User directory. The JavaScript used for visualisation can be found in .User/templates/User/userView.html.

## Dependencies
### You must have Python 3.6 or higher.
Check python version:
```
$ python --version
```
###  You must have Django installed to run the development server along with the following libraries (django-crispy-forms, PyGithub, regex)
Install Requirements
```
pip install -r requirements.txt
```

## Run server
Run website on local machine.
Navigate into the Github_Access directory and run manage.py with the runserver option. This website can then be accessed on http://127.0.0.1:8000.
```
$ python manage.py runserver
```