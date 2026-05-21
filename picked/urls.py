from django.urls import path
from picked.views import add_to_favorite, favorite_list


app_name = 'picked'

urlpatterns = [
    path('favorite/<int:pk>/', add_to_favorite, name='favorite'),
    path('favorite_list', favorite_list, name='favorite_list')
]