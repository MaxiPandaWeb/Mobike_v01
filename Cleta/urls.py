from django.urls import path
from django.conf.urls import url
from Cleta import views

urlpatterns = [
    path('', views.register, name='register'),
    path('index', views.mostrar, name='index'),
    path('pagos', views.pagos, name='pagos'),
    path('pago1', views.pago1, name='pago1'),
    path('pago2', views.pago2, name='pago2'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
