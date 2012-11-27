# Django and South migrations shorthands

- date: 2012-11-27
- category: python
- tags: python, django, south

------

Just decided to share my shorthands I use with [Django][] and [South][] migrations.

Inside of your  **.bash_aliases** file just add the following lines of code

````sh
function imig() {
    python manage.py schemamigration "$@" --initial;
}

function mig() {
    clear;
    python manage.py schemamigration "$@" --auto;
    python manage.py migrate "$@";
}
````

+ **imig** is used when you first start using migrations for some [Django][] application;
+ **mig** is used for further migrations


#### Usage
+ Lest say you have application called **my_app** and you want to use schema evolution then you just type

````sh
(env) super_project $ imig my_app
````
This produces a file **0001_initial.py** under **my_app/migrations** folder

+ Since you change your database scheme, for further migrations you just use the second command

````sh
(env) super_project $ mig my_app
````


Hope this will help you.

[django]: http://djangoproject.com
[south]: http://south.aeracode.org/
