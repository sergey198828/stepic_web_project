from django.conf.urls import url
import views

urlpatterns = [
    # /login/
    url(r'^login/$', views.stub, name="sign-in"),
    # /signup/
    url(r'^signup/$', views.stub, name="sign-up"),
    # /question/<123>/
    url(r'^question/(\d+)/$', views.question, name="view-question"),
    # /ask/
    url(r'^ask/$', views.stub, name="ask-question"),
    # /popular/
    url(r'^popular/$', views.stub, name="top-questions"),
    # /new/
    url(r'^new/$', views.stub, name="latest-questions"),
]
