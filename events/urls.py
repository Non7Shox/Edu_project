from django.urls import path
from events.views import EventsListView

app_name = 'events'

urlpatterns = [
    path('', EventsListView.as_view(), name='list')
]
