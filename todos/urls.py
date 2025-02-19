from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "todos"

urlpatterns = [
    # path('tasks/', include(router.urls)),  # Include router-generated URLs
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
