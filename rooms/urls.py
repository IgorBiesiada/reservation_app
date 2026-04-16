from django.urls import path


from .views import AddSportsResourceView, EditSportResourceView, ResourceListView, AddOfficeResourceView, DeleteResourceView

app_name = 'rooms'

#addresses to subpages
urlpatterns = [
    path('add_sport/', AddSportsResourceView.as_view(), name="add_sport"),
    path('<pk>/edit_sport/', EditSportResourceView.as_view(), name="edit_room"),
    path('', ResourceListView.as_view(), name='resource_list'),
    path('add_office', AddOfficeResourceView.as_view(), name="add_office"),
    path('<pk>/delete_recource', DeleteResourceView.as_view(), name="delete_resource")
]
