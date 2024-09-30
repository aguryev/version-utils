from django.conf.urls import url

from .views import MoonshotUtilsVersionView


urlpatterns = [
    url("version/", MoonshotUtilsVersionView.as_view(), name="moonshot-utils-version"),
]
