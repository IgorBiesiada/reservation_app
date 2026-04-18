from django.urls import path


from .views import (AddSportsResourceView, 
                    EditSportResourceView, 
                    ResourceListView, 
                    AddOfficeResourceView,
                    EditOfficeResourceView, 
                    DeleteResourceView, 
                    AddEventResourceView, 
                    EditEventResourceView,
                    AddBeautyResourceView,
                    EditBeautyResourceView,
                    AddLivingResourceView,
                    EditLivingResourceView 
                    )

app_name = 'rooms'

#addresses to subpages
urlpatterns = [
    path('/add_sport/', AddSportsResourceView.as_view(), name="add_sport"),
    path('/<pk>/edit_sport/', EditSportResourceView.as_view(), name="edit_sport"),
    path('', ResourceListView.as_view(), name='resource_list'),
    path('/add_office', AddOfficeResourceView.as_view(), name="add_office"),
    path('/<pk>/edit_office', EditOfficeResourceView.as_view(), name="edit_office"),
    path('/<pk>/delete_recource', DeleteResourceView.as_view(), name="delete_resource"),
    path('/add_event', AddEventResourceView.as_view(), name="add_event"),
    path('/<pk>/edit_event', EditEventResourceView.as_view(), name="edit_event"),
    path('/add_beauty', AddBeautyResourceView.as_view(), name="add_beauty"),
    path('/<pk>/edit_beauty', EditBeautyResourceView.as_view(), name="edit_beauty"),
    path('add_living', AddLivingResourceView.as_view(), name="add_living"),
    path('/<pk>/edit_living', EditLivingResourceView.as_view(), name="edit_living")
]
