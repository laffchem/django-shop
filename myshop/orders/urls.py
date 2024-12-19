from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("create/", views.order_create, name="order_create"),
    path("created/<uuid:order_id>/", views.order_created_view, name="order_created"),
]
