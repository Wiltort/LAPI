#  импортируйте в код всё необходимое
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/v1/posts/', views.api_posts),
    path('api/v1/posts/<int:id>/', views.api_posts_detail),
    path('api/v1/api-token-auth/', obtain_auth_token),
]
