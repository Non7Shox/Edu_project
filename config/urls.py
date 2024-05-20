from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('classes/', include('classes.urls', namespace='classes')),
    path('events/', include('events.urls', namespace='events')),
    path('shop/', include('shop.urls', namespace='shop')),
]
