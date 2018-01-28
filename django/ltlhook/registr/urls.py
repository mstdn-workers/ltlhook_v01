from django.conf.urls import url, include

from . import views
app_name = 'registr'
urlpatterns = [
    # ex: /polls/
    #url('', views.index, name='index'),
    url('reg/', views.registration, name='reg'),
    url('result/', views.result, name='result'),
    url('recv', views.recv, name='recv'),
]
