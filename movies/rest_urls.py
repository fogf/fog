from django.conf.urls import url, include
import movies.urls


urlpatterns = []

urlpatterns += movies.urls.rest_urls