from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name="contact-us-page"),
    path('profile/', views.CreateProfileView.as_view(), name="create-profile-page"),
    path('profile-list/', views.ProfilesView.as_view(), name="profile-list-page"),

]
