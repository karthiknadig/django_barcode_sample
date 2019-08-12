from django.urls import path
from pybarc.views import home, handle_image

urlpatterns = [
    path('', home, name='home'),
    path('img/<prodcode>', handle_image, name='handle_image')
]