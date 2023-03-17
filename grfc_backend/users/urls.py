from django.urls import path, include

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .views import SubdivisionViewSet, UserLoginView, HomeView, SubdivisionAPIView, SubdivisionAPIList  # noqa 501
from django.contrib.auth.decorators import login_required
from rest_framework import routers

app_name = 'users'

router = routers.SimpleRouter()
router.register(r'subdivision', SubdivisionViewSet)

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('auth/', LoginView.as_view(template_name='users/auth.html'), name='login'),  # noqa 501
    path('logout/', LogoutView.as_view(), name='logout'),
    path('filter/', login_required(TemplateView.as_view(template_name='index.html')), name='filter'),  # noqa 501
    path('api/v1/', include(routers.urls))
    # path('api/v1/subdivision/', SubdivisionViewSet.as_view({'get': 'list'})),
    # path('api/v1/subdivision/<int:pk>/', SubdivisionViewSet.as_view({'put': 'update'})),
]
