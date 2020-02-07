"""challenges URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings


# The URLs of our `challenges` project
urlpatterns = [
    url(r'api/', include('backend.urls', namespace='api')),
    url(r'admin/', admin.site.urls),
]


# The Django Debug Toolbar is a configurable set of panels that display
# various debug information about the current request/response and when clicked

if settings.DEBUG:
    import debug_toolbar

    # update the list `urlpatterns`
    urlpatterns = [
        url(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


# Error message - 404 - Not Found
# The page_not_found() view is overridden by handler404
handler404 = 'backend.views.error_404'
