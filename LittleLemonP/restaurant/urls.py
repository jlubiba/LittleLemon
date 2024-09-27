from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)
router.register(r"booking", views.BookingViewSet, basename="bookings")
router.register(r"menu", views.BookingViewSet, basename="menu")
# router.register(r"home", views.index, basename="home")

urlpatterns = [
    path("", views.index, name="home"),
    # path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu_item"),
    # path("menu/items", views.MenuItemView.as_view(), name="menu_items"),
    path("api-token-auth/", obtain_auth_token),
]

urlpatterns += router.urls