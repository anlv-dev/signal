from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='reigister' ),
    path('profle/', views.profile, name='profile' ),
]
