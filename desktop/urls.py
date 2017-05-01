from django.conf.urls import url
from views import load_desktop, order_details
urlpatterns = [
    url(r'^$', load_desktop),
    url(r'^order/(?P<order_id>[0-9])/$', order_details)
]
