from django.urls import path
from userprofile import views

urlpatterns = [
    # Profile page (GET and POST for edit/save)
    path("", views.user_profile, name="profile"),
    # Network page
    path("network/", views.network, name="network"),
]
