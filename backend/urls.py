"""compile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from backend import views
from django.conf.urls import url


urlpatterns = [
    url(r'users-data/', views.UserDataSet.as_view()),
    url(r'get-data/', views.GetUserDataSet.as_view()),
    url(r'get-top-10-pages/', views.GetTop10PagesSet.as_view()),
    url(r'get-top-10-countries/', views.GetTop10CountriesSet.as_view()),
    url(r'get-top-10-browsers/', views.GetTop10BrowsersSet.as_view()),
    url(r'get-top-10-screen-resolution/', views.GetTop10ScreenResolutionsSet.as_view()),
    url(r'get-filter-data-set/', views.GetFilterDataSet.as_view()),

]
