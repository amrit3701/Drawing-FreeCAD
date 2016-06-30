from django.conf.urls import url

from . import views

urlpatterns = [
    #directs to index veiw
    url(r'^$', views.index, name='index'),
    url(r'^/specs/$', views.specs, name='specs'),
    url(r'^/specs/$', views.download, name='download')
]
