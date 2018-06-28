"""detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from school.views import home,studentDetail,StudentList,Index,CreateProject,CreateStudent,UpdateStudent,DeleteStudent,UpdateProject,DeleteProject,studentTest,pred
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^student/(?P<id>\d+)/', studentDetail,name='student_detail'),
    url(r'^test/(?P<id>\d+)/', studentTest,name='student_test'),
    url(r'^list/', StudentList.as_view(),name='student_list'),
    url(r'^backstage/$', Index.as_view(), name='index'),
    url(r'^create/project/', CreateProject.as_view(), name='create_project'),
    url(r"^create/student/", CreateStudent.as_view(), name='create_student'),
    url(r'^update/student/(?P<pk>\d+)/', UpdateStudent.as_view(), name='update_student'),
    url(r'^delete/student/(?P<pk>\d+)/', DeleteStudent.as_view(), name='delete_student'),
    url(r'^update/project/(?P<pk>\d+)/', UpdateProject.as_view(), name='update_project'),
    url(r'^delete/project/(?P<pk>\d+)/', DeleteProject.as_view(), name='delete_project'),
    url(r'^pred/', pred,name='pred'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 