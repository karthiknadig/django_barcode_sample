from django.urls import path
from pybarc.views import home, handle_image

urlpatterns = [
    path('', home, name='home'),
    path('product/<prodcode>', handle_image, name='handle_image')
]