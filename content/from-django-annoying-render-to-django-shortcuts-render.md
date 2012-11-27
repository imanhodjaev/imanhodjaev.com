# From annoying.render_to to django shortcuts.render

- date: 2012-11-27
- category: python
- tags: python, django, render

------


Few months ago I figured out that I use only **render_to** decorator from **[django-annoying][]** package.

````python
from annoying.decorators import render_to

@render_to('some-template.html')
def some_view(request):
    return {'var1': 1}
````

And so far switched to **render** function from **django.shortcuts**

````python
from django.shortcuts import render

def some_view(request, template='some-template.html'):
    return render(request, template, {'var1': 1})
````

This is much cleaner as well as much simpler.


[django-annoying]: https://bitbucket.org/offline/django-annoying/wiki/Home
