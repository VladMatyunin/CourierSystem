from django.conf.urls import url
from views import load_cabinet
urlpatterns = [
    url(r'^main', load_cabinet)
]