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
                    EditLivingResourceView,
                    edit_resource,
                    detail_resource 
                    )

app_name = 'rooms'

#addresses to subpages
urlpatterns = [
    path('add_sport/', AddSportsResourceView.as_view(), name="add_sport"),
    path('', ResourceListView.as_view(), name='resource_list'),
    path('/add_office', AddOfficeResourceView.as_view(), name="add_office"),
    path('delete/<int:pk>/', DeleteResourceView.as_view(), name="delete"),
    path('/add_event', AddEventResourceView.as_view(), name="add_event"),
    path('/add_beauty', AddBeautyResourceView.as_view(), name="add_beauty"),
    path('add_living', AddLivingResourceView.as_view(), name="add_living"),
    path('edit_resource/<int:pk>', edit_resource, name="edit_resource"),
    path('resource_detail/<int:pk>', detail_resource, name='resource_detail')
]
