# Django serving media files for local development

- date: 2013-03-03
- category: django
- tags: python, django, media

------

## You need to serve you local media files while developing a project, just add the following code into your main urls.py file.


### urls.py
````python
if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
````
