from django.urls import path
from . views import CreateUserView, LoginUserView, logout_view


app_name = 'users'


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]