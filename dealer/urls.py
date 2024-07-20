from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from dealer import views

router = routers.DefaultRouter()
router.register(r'dealers', views.DealerView, 'dealers')

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", include_docs_urls(title="Dealer API"))
]