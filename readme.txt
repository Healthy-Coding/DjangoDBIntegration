This repository includes the binding settings in the Univ/settings.py file that connects Django and MySQL. MySQL will need to be installed locally.

Open a terminal, cd into the directory that contains manage.py file. Run >>python manage.py runserver

The Database settings are speciic to my local MYSQL db, you will have to change the user and password to your settings.

After changing those settings, you should be prompted to open a local host URL.

The Univ directory contains the main urls.py and settings.py files.

The ListIndex directory is a Django app that for now lists statistics of Georgia Universities. See models.py, urls.py, views.py for details.