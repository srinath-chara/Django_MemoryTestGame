from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='memory-start'),
    path('input', views.input, name='memory-input'),
    path('q1', views.q1, name='memory-q1'),
    path('q2', views.q2, name='memory-q2'),
    path('q3', views.q3, name='memory-q3'),
    path('q4', views.q4, name='memory-q4'),
    path('q5', views.q5, name='memory-q5'),
   
    path('iscorrect1', views.iscorrect1, name='memory-iscorrect'),
]
