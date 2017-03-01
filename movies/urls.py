from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'movie', views.MovieViewSet)
router.register(r'celebrity', views.CelebrityViewSet)

rest_urls = router.get_urls()
