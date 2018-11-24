from django.urls import path
from .views import HomeView,RSVPView,GalleryView,ContactCreateView

app_name ='wedding'
urlpatterns = [
    path('rsvp/', RSVPView.as_view(), name='rsvp'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('contact_us/',ContactCreateView.as_view(),name='contact'),
]
