"""timesheets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dbo.views import employee , project , timesheets , view_projects, Aproove_project, Aproove_projectt
from login.views import home , user_login , logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home , name = 'home'),
    url(r'^login/', user_login),
    url(r'^employeedetail/', employee),
    url(r'^view/', view_projects),
    url(r'^projectdetail/', project),
    url(r'^create-timesheet/', timesheets ),
    #url(r'^create-timesheet/', timesheets , name='timesheet'),
    url(r'^aproove-project/', Aproove_project, name = 'Aproove_project'),
    url(r'^aproove-projectt/(?P<id>[\w-]+)/$', Aproove_projectt , name = 'timesheet'),
    url(r'^logout/', logout),

]
