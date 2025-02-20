from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = "todos"

urlpatterns = [
    # path('tasks/', include(router.urls)),  # Include router-generated URLs
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('login/', auth_views.LoginView.as_view(template_name='todos/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page="todos:index"), name='logout')
    # path('logout/', views.user_logout, name='logout')
]
