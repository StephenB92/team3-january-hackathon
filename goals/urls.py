from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_goals, name='all_goals'),
    path('<int:goal_id>/', views.goal_detail, name='goal_detail'),
    path('add/', views.add_goal, name='add_goal'),
    path('edit/<int:goal_id>/', views.edit_goal, name='edit_goal'),
    path('delete/<int:goal_id>/', views.delete_goal, name='delete_goal')
]

