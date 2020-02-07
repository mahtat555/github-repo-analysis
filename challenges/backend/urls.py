"""backend URL Configuration

The `urlpatterns` list routes URLs to views. This module is pure Python code
and is a mapping between URL path expressions to Python functions (your views).
"""

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from backend import views


# Namespace for `backend` application
app_name = 'api'

# The URLs of our `backend` application.
urlpatterns = [
    ## Index page
    # `http://127.0.0.1:8000/api/`
    url(r'^$', views.index, name="index"),
    # `http://127.0.0.1:8000/api/index/`
    url(r'^index/$', views.index, name="index"),

    # Help page
    # `http://127.0.0.1:8000/api/help/`
    url(r'^help/$', views.help, name="help"),

    ## List of  100 trending public repos on GitHub and languages used
    # `http://127.0.0.1:8000/api/repositories/`
    url(r'^repositories/$', views.repositories, name="repositories"),

    ## Lists languages for the specified repository.
    # `http://127.0.0.1:8000/api/repository/<id>/`
    url(r'^repository/(?P<id>\d+)/$', views.repository, name="repository"),

    ## Number of repos using a language
    # `http://127.0.0.1:8000/api/number/?language=<language>/`
    url(r'^number/$', views.number_repos, name="number_repos"),

    ## The list of repos using a language
    # `http://127.0.0.1:8000/api/list/?language=<language>/`
    url(r'^list/$', views.list_repos, name="list_repos"),

    ## Frameworks popularity over the 100 repos
    # `http://127.0.0.1:8000/api/popularity/?language=<language>/`
    url(r'^popularity/$', views.popularity, name="popularity"),

    ## Plotting Results
    # `http://127.0.0.1:8000/api/popularity/plot/?language=<language>/`
    url(r'^popularity/plot/$', views.plot, name="plot"),
]
