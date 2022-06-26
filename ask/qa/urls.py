from django.conf.urls import url
from .views import home, stub, question

urlpatterns = [
    # /
    url(r'^$', home, name="sign-in"),
    # /login/
    url(r'^login/$', stub, name="sign-in"),
    # /signup/
    url(r'^signup/$', stub, name="sign-up"),
    # /question/<123>/
    url(r'^question/(\d+)/$', question, name="view-question"),
    # /ask/
    url(r'^ask/$', stub, name="ask-question"),
    # /popular/
    url(r'^popular/$', stub, name="top-questions"),
    # /new/
    url(r'^new/$', stub, name="latest-questions"),
]
