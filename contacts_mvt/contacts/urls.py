from django.urls import path
from .views import *

urlpatterns = [
  path("", contacts_list, name="contacts_list"),
  path("contacts/<int:id>", contact_detail, name="contact_detail"),
  path("contacts/create", contact_create, name="contact_create"),
  path("contacts/update/<int:id>", contact_update, name="contact_update"),
  path("contacts/delete/<int:id>", contact_delete, name="contact_delete")
]