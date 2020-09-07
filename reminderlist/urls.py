from django.urls import path
from reminderlist import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>/',views.activity,name='get_activity'),
    path('create/',views.create,name='create_activity'),
    path('delete/<int:pk>/',views.delete,name='delete_activity'),
    path('wall/',views.wall,name='wall'),
    path('post/<int:pk>/comment/', views.comment, name='comment'),

]