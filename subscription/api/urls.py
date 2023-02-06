from home.views import BlogView
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register(r'blog', BlogView, basename='blog')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]