from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^checkout$',views.checkout),
    url(r'^buy/(?P<item_id>\d+)$',views.buy),
    url(r'^go_back$',views.go_back)
]