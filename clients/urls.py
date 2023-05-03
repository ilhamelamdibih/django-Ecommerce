from django.urls import path
from . import views
urlpatterns = [
    path('register/',
        views.ClientRegistrationView.as_view(),
        name='client_registration'),
]