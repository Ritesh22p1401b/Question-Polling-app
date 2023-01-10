from django.urls import path
from .import views

urlpatterns=[
    path('',views.home_main,name='home'),
    path('question',views.create_question,name='question'),
    path('profile/<str:pk>/',views.user_profile,name='profile')
]
