
I am trying the following filtering app.

https://github.com/modlinltd/django-advanced-filters/issues/14
https://github.com/modlinltd/django-advanced-filters

2016-03-17:
I have a problem getting the field list to show any fields.

https://github.com/modlinltd/django-advanced-filters/issues/14




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Title:  . Copy of my issue post...

-----------------------2016-03-17[Mar-Thu]16-11PM

Thankyou for your efforts on this feature!

## My Issue:
I see the filter form, but it says the following in the field dropdown.

"Or (mark an or between blocks)"

Screen shot attached.

Can someone help me understand what I am doing wrong?

thanks,

### My Installation.

I installed django edge.
Then installed modlinltd/django-advanced-filters

### Info:

Django 1.8.11
Windows.

### My code in admin.py:

> from advanced_filters.admin import AdvancedFilterAdmin, AdminAdvancedFiltersMixin
>   
> class Cilisting1Admin( AdminAdvancedFiltersMixin, admin.ModelAdmin ):
> 
>  .....  some other stuff ....
>
> list_filter = (
>     'wc_idea_date',
>     'actual_implementation_date',
>     )
> 
> advanced_filter_fields = (
>     'owner',  'originator',  'project_number',
>     )



___________




### My installation steps. (Possibly unneeded detail)

http://django-edge.readthedocs.org/en/latest/#quick-start
 
 django-admin.py startproject --template= \
       https://github.com/arocks/edge/archive/master.zip -extension=py,md,html,env    my_proj
 cd my_proj
 pip install -r requirements.txt 
 cd src
 cp my_proj/settings/local.sample.env my_proj/settings/local.env
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver 0.0.0.0:8000

 python manage.py startapp cilist1
 edit cilist1 models.py
 edit base.py - add clist1 app
 python manage.py makemigrations cilist1
 python manage.py sqlmigrate cilist1 0001
 python manage.py makemigrations 
 python manage.py migrate
 edit cilist1 admin.py
 python manage.py runserver 0.0.0.0:8000

 An aside... I moved to Windows...
 set wpip=c:\p2\Python27\Scripts\pip
 %wpip% install -r requirements.txt
 cd src
 python manage.py runserver 0.0.0.0:8000

 %wpip% install django-advanced-filters

 Install from pypi: pip install django-advanced-filters
 Add both 'advanced_filters' and 'easy_select2' to INSTALLED_APPS.
 Add url(r'^advanced_filters/', include('advanced_filters.urls')) to your project's urlconf.
 Run python manage.py syncdb

 %wpip% install django-grappelli
 added grapelli to installed apps.




=====
______
______

![issue--fields not showing in advanced filter modlinltd](https://cloud.githubusercontent.com/assets/4622715/13858107/7d8a16ba-ec53-11e5-8a3f-3a76208c72ad.png)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
