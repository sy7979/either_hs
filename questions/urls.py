from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete/', views.delete, name='delete'),

    path('<int:id>/comments/', views.comments, name='comments'),

    path('<int:id>/edit/', views.edit, name='edit'),
    path('lists/',views.lists,name='lists'),

    path('<int:question_id>/comments_delete/<int:choice_id>/', views.comments_delete, name='comments_delete')
]
