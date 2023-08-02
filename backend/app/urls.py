from django.urls import path
from . import views


urlpatterns = [path("send", views.caleander.as_view(), name="CalApi")]
