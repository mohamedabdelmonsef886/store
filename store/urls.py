from django.urls import path
from . import views
app_name = 'store'  # <<< دي مهمة جدًا
urlpatterns = [
    path('', views.home, name='home'),
]
