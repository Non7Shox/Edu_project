from django.urls import path
from pages.views import HomePageView, ContactListView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactListView.as_view(), name='contact'),
]
