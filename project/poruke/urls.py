from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index, name='poruke_index'),
    path('int/<int:br>', views.broj, name='poruke_broj'),
    path('rec/<str:rec>', views.rec, name='poruke_rec'),
    path('params/', views.params, name='poruke_params'),
    #regex validacija unosa
    re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))', views.regex, name='poruke_regex'),
    path('hello/', views.hello, name='poruke_hello'),
]
