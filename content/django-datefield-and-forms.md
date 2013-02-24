# Working with forms and DateField in Django

- date: 2013-02-24
- category: django
- tags: python, django, forms

------

## Missing form DateField/DateTimeField field

Lets say you have the following model and  forms

### model
````python
class MyModel(models.Model):
    field = forms.CharField(max_length=100)
    expires = forms.DateField(auto_now_add=True)
````

### Form
````python
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
````

So then if you try to render field **expires** within a template you'll see nothing.
All this because of **[auto_now_add][]** parameter.

    Note
    As currently implemented, setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.

Finally you just have to remove **auto_now_add** parameter if you want to display this field in the form.

[auto_now_add]: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.DateField.auto_now_add
