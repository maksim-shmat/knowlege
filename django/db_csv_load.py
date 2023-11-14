"""Load db from csv."""

#1 blahblah create project

1. Create a Django project called juggler.
2. Create a Django app called projectp.
3. Add the app projects to the juggler/settings.py file
4. Create two related model classes called Project and Task in projectp/models.py
5. Create migration scripts and migrate the models definition to the database.
6. Open Django shell and import models.
7. Populate the database with an example and write a query displaying the list
of tasks associated with a given project.

#2 Populating the Book project's db

1. Create folder structure inside the project dir:
    bookr/reviews/management/commands/

2. Create loadcsv.py  # check "Custom management commands" in docs.djangoproject.com

3. Recreate a fresh db. Delete the SQL db file:
    rm db.sqlite3

4. Create fresh db with migrate:
    python manage.py migrate

5. Execute the loadcsv custom management command to populate the db:
    python manage.py loadcsv --csv reviews/management/commands/
    WebDebWithDjangoData.csv
