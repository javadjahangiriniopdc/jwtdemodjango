from django.urls import include, path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [        
    path('api/users/create/', views.UserCreateAPIView.as_view(), name='create'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/hello/', views.HelloAPI.as_view(), name = 'hello_api'),
    path('api/hello2/', views.hello_drf, name='hello_api2'),  

    path('api/hellorole/', views.HelloRoleAPI.as_view(), name = 'hello_role_api'),
    path('api/hellorole2/', views.hello_role_drf, name='hello_role_api2'),   

]