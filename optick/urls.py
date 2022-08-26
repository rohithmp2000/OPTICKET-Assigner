"""optick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf  import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.form),
    path('header/',views.header),
    path('home/',views.home),
    path('adminheader/',views.adminheader),
    path('doctorheader/',views.doctorheader),
    path('labheader/',views.labheader),
    path('patientheader/',views.patientheader),
    path('publicheader/',views.publicheader),
    path('adminhome/',views.adminhome),
    path('doctorhome/',views.doctorhome),
    path('labhome/',views.labhome),
    path('patienthome/',views.patienthome),
    path('appointment/',views.appointment),
    path('adddept/',views.adddept),
    path('patientregister/',views.patientregister),
    path('registercomplaint/',views.registercomplaint),
    path('publichome/',views.publichome),
    path('adddept1/',views.adddept1),
    path('regcomplaint/',views.regcomplaint),
    path('staffappoint/',views.staffappoint),
    path('remove_dept/',views.remove_dept),
    path('remove_dept1/<int:id>', views.remove_dept1),
    path('regpatient/',views.regpatient),
    path('givecomplaint/',views.givecomplaint),
    path('givecomplaint1/',views.givecomplaint1),
    path('searchdept/',views.searchdept),
    path('searchdept1/',views.searchdept1),
    path('removestaff/',views.removestaff),
    path('removestaff1/<int:id>',views.removestaff1),
    path('drallotment/',views.drallotment),
    path('doctorallotment1/<int:id>',views.doctorallotment1),
    path('drallotment3/',views.drallotment3),
    path('login1/',views.login1),
    path('login2/',views.login2),
    path('opallot1/',views.opallot1),
    path('opallot3/<str:id>',views.opallot3),
    path('opdays1/<int:id>',views.opdays1),
    path('opdays4/',views.opdays4),
    path('viewdoctor/<str:id>',views.viewdoctor),
    path('viewop/<str:id>',views.viewop),
    path('viewdoctor1/<str:id>',views.viewdoctor1),
    path('viewop1/<str:id>',views.viewop1),
    path('collectop/<int:id>',views.collectop),
    path('collectop1/',views.collectop1),
    path('opid/',views.opid),
    path('patdetails/<str:id>',views.patdetails),
    path('diagnosis/<str:id>',views.diagnosis),
    path('diagnosis1/',views.diagnosis1),
    path('labtest/<str:id>',views.labtest),
    path('labtest1/',views.labtest1),
    path('medicine1/',views.medicine1),
    path('leave/',views.leave),
    path('leave1/',views.leave1),
    path('changestaff1/<int:id>',views.changestaff1),
    path('changestaff2/',views.changestaff2),
    path('logout/',views.logout),
    path('viewcomplaint/',views.viewcomplaint),
    path('report1/',views.report1),
    path('report2/',views.report2),
    path('viewtest/',views.viewtest),
    path('viewtest1/<int:id>',views.viewtest1),
    path('viewtest2/<int:id>',views.viewtest2),
    path('viewresult/',views.viewresult),
    path('viewresultdoctor/',views.viewresultdoctor),
    path('viewresultdoctor1/<str:id>',views.viewresultdoctor1),
    path('confirm/',views.confirm),
 


















]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)