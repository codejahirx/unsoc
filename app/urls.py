from django.urls import path

from app import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:pk>/', views.user_details, name='user_details'),
    path('<int:pk>/suspend/', views.suspend_user, name='suspend_user'),
    path('<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
]
