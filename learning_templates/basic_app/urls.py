from django.urls import path, include
from . import views

#Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('basic_app/',views.index,name='index'),
    path('basic_app/index',views.index,name='index'),
    path('basic_app/relative/',views.relative,name='relative'),
    path('basic_app/other/',views.other,name='other'),
]