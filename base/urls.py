from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>', views.room, name='room'),
    path('profile/<str:pk>', views.user_profile, name='user-profile'),

    path('create_room', views.create_room, name='create-room'),
    path('delete_room/<str:pk>', views.delete_room, name='delete-room'),
    path('delete_message/<str:pk>', views.delete_message, name='delete-message'),

    path('update_user/', views.update_user, name='update-user'),
    path('update_room/<str:pk>', views.update_room, name='update-room'),

    path('topics/', views.topics_page, name='topics'),
    path('activity/', views.activity_page, name='activity'),
]
