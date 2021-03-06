from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('api/user', views.UserList.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/create_hood',views.HoodList.as_view()),
    path('api/v1/hoods', views.AllHoodsList.as_view()),
    path('api/v1/view_hood/<int:pk>', views.SingleHoodList.as_view()),
    path('api/v1/post', views.CreatePostView.as_view()),
    path('api/v1/create_business/<int:pk>', views.CreateBusinessView.as_view()),
    path('api/v1/create_dept/<int:pk>', views.CreateDepartmentView.as_view()),
    path('api/v1/profile/<int:pk>/<int:id>', views.EditProfileView.as_view())
    
]