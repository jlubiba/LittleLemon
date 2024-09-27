from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)
router.register(r"booking", views.BookingViewSet, basename="bookings")
router.register(r"menu", views.BookingViewSet, basename="menu_items")

urlpatterns = [
    path("", views.index, name="home"),
    path("api-token-auth/", obtain_auth_token),
]

urlpatterns += router.urls