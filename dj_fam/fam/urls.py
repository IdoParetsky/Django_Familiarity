from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('fam', viewset=views.Fam)


urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls))
    #path('get_human', views.get_human, name='get_human'),
    #path('get_all', views.get_all, name='get_all'),
    #path('add', views.add_human, name='add_human')
]
