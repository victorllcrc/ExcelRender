from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('hola',views.ReporteExcel.as_view(), name='chupetin')
]