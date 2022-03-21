from django.urls import path
from GlaCine import views

app_name = 'GlaCine'

urlpatterns = [
    path('', views.jump_page, name='jump_page'),
    path('<int:page>/', views.index, name='index'),
    path('cinema/<slug:cinema_name>/', views.cinema, name ='cinema'),
    path('review/', views.review, name ='review'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
]