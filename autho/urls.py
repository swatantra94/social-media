from django.urls import path 
from autho import views


urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup,name='signup')
]