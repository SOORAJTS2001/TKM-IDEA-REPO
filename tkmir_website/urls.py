from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('login_register/',views.log_reg,name='log-reg'),

]