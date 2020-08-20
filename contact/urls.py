from django.urls import path
from .views import ContactList, ContactAlterView
urlpatterns = [
    path("", ContactList.as_view(), name="Contact-list"),
    path("<int:id>/", ContactAlterView.as_view())
]
