from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'teste/$', views.post_list),
    # path('', views.post_list, name='post_list'),

    url(r'novo_jogo/$', views.novo_jogo),
    url(r'partida', views.partida),
    url(r'principal', views.principal),
    path('', views.novo_jogo, name='novo_jogo'),
]