from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views # new
 
 
urlpatterns = [
    url(r'^add/$', calc_views.add, name='add'),  # new
    url(r'^add/(\d+)/(\d+)$', calc_views.add2, name='add2'), # new
    url(r'^admin/', admin.site.urls),
]