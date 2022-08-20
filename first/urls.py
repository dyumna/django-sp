from django.urls import path, include

from . import views
from .rest_api import router

urlpatterns = [
    # path('', views.tst),
    path('<int:book_id>/', views.detail),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]

