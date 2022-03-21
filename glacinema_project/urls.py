from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from GlaCine import views

urlpatterns = [
    path('', views.jump_page, name='jump_page'),
    path('GlaCine/', include('GlaCine.urls')),
    path('review/', views.review, name ='review'),
    path('login/', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
