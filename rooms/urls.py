from django.urls import path


from rooms.views import (DeleteResourceView, 
                        edit_resource,
                        detail_resource,
                        AddResourceView,
                        ResourceListView
                    )

app_name = 'rooms'

#addresses to subpages
urlpatterns = [
    path('add/<str:resource_type>/', AddResourceView.as_view(), name="add_resource"),
    path('', ResourceListView.as_view(), name='resource_list'),
    path('delete/<int:pk>/', DeleteResourceView.as_view(), name='delete'),
    path('edit_resource/<int:pk>', edit_resource, name="edit_resource"),
    path('resource_detail/<int:pk>', detail_resource, name='resource_detail')
]
