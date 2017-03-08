This repository includes the binding settings in the Univ/settings.py file that connects Django and the MySQL server located on Amazon Web Services. MySQL will need to be installed locally. Once MySQL is installed locally, pip install mysqlclient to bind MySQL and Django. Follow this tutorial if you need some guidance (http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-mysql-for-django). I ran into difficulties with installing MySQL locally, others had difficulty pip installing mysqlclient, we eventually found solutions by Googling and stack overflowing it. If you’re having trouble with the Django DB API drivers like mysqlclient, here is a good place to refer to (https://docs.djangoproject.com/en/1.10/ref/databases/).

For security reasons, the username and passwords are stored in user.py file. Ask someone in Healthy-Coding group for this information.

Open a terminal, cd into the directory that contains manage.py file. Run >>python manage.py runserver

You should be prompted to open a local host URL. Add “/ListIndex” to that local URL to see the ListIndex page.

The ListIndex directory is a Django app that for now lists statistics of Georgia Universities. See models.py, urls.py, views.py for details.

Extra Information:
The Univ directory contains the main urls.py and settings.py files.

