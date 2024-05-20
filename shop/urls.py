from django.urls import path
from shop.views import ShopListView

app_name = 'shop'

urlpatterns = [
    path('', ShopListView.as_view(), name='list'),
]
