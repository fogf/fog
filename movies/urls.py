from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

rest_urls = router.get_urls()
