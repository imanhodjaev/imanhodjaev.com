# Django working with forms in real life - part 1

- date: 2012-11-25
- category: python
- tags: python, django, forms

------

When newbies in Django start working with forms they often use checking of **request.method** for **GET** or **POST**.
Lets assume you have a view called **create_item**

````python
def create_item(request):
    if request.method == 'POST':
        form = SomeForm(request.POST)

        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        # do something
````

So its valid and this kind of code works just fine and in real life this code gets shorter

````python
def create_item(request):
    form = SomeForm(request.POST or None)

    if form.is_valid():
        form.save()
````

This code is more clear and easier to understand.

Thats all for the first part of "how to work with form" series.
I decided to write a small bit at a time
so you don't get confused.


Enjoy!
