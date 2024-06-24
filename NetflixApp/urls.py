from django.urls import path

from NetflixApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('movie/<str:pk>', views.movies, name='movie'),
    path('genre/<str:pk>/', views.genre, name='genre'),
   path('my-list', views.my_list, name='my-list'),
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('search', views.search, name='search'),  


]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)