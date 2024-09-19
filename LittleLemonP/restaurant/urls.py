from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register("booking", views.BookingViewSet, basename="bookings")

urlpatterns = [
    path("", views.index, name="home"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu_item"),
    path("menu/items", views.MenuItemView.as_view(), name="menu_items"),
]

urlpatterns = router.urls