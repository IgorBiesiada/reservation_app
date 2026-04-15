from django.urls import path


from .views import AddSportsResource, EditSportResource, ResourceListView

app_name = 'rooms'

#addresses to subpages
urlpatterns = [
    path('add_sport/', AddSportsResource.as_view(), name="add_sport"),
    path('<pk>/edit_sport/', EditSportResource.as_view(), name="edit_room"),
    path('', ResourceListView.as_view(), name='resource_list'),
    # path('room/delete/<int:room_id>/', DeleteRoomView.as_view(), name="delete-room"),
    # path('room/modify/<int:id>/', RoomModifyView.as_view(), name="update-room"),
    # path('room/reserve/<int:room_id>', ReservationView.as_view(), name='reservation'),
    # path('room/detail/<int:room_id>/', DetailRoomView.as_view(), name='room-detail'),
    # path('room/search/', RoomSearchView.as_view(), name='room-search')
]
