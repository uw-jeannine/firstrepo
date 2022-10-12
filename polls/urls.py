from django.urls import path
from .import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name='home'),
    path('form', views.form, name='form'),
    path('registration', views.registration, name='registration'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/update', views.update, name='update'),
    path('/student', views.student, name='student'),
    path('ussd/', views.ussdapp, name='ussd'),
    path('idaussd', views.idaussd, name='idauss')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)