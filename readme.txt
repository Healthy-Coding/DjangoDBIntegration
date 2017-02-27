This repository includes the binding settings in the Univ/settings.py file that connects Django and MySQL located on Amazon Web Services. MySQL will need to be installed locally.

For security reasons, the username and passwords are stored in user.py file. Ask someone in Healthy-Coding group for this information.

Open a terminal, cd into the directory that contains manage.py file. Run >>python manage.py runserver

After changing those settings, you should be prompted to open a local host URL. Add “/ListIndex” to that local URL to see the ListIndex page.

The Univ directory contains the main urls.py and settings.py files.

The ListIndex directory is a Django app that for now lists statistics of Georgia Universities. See models.py, urls.py, views.py for details.