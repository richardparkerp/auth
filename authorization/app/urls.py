from django.urls import path
from .views import *

    
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', CreatePost.as_view(), name='create'),
]
