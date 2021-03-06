from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from solapp.views import  LoginView, RegisterView,ProfilePage
from solapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('admin-person/', views.adminperson), 
    path('time/',views.time),
    path('time/morning/',views.Vu),
    path('time/evening/',views.VU),
    path('time/morning/Osh/nabor/',views.aS),
    path('time/morning/Bi/nabor/',views.AS),
    path('time/morning/Uz/nabor/',views.As),
    path('time/evening/Osh/nabor/',views.aSd),
    path('time/evening/Bi/nabor/',views.ASD),
    path('time/evening/Uz/nabor/',views.AsD),
    path('PersonBCOsh/create/', views.mgcreateBcOsh),
    path('PersonBCOsh/<id>/delete/', views.mgdeleteBcOsh ),
    path('PersonBCOsh/<id>/update/', views.mgupdateBcOsh),
    path('PersonFronOsh/create/', views.mgcreateFronOsh),
    path('PersonFronOsh/<id>/delete/', views.mgdeleteFronOsh ),
    path('PersonFronOsh/<id>/update/', views.mgupdateFronOsh),
    path('PersonFullOsh/create/', views.mgcreateFullOsh),
    path('PersonFullOsh/<id>/delete/', views.mgdeleteFullOsh ),
    path('PersonFullOsh/<id>/update/', views.mgupdateFullOsh),
    path('PersonUIOsh/create/', views.mgcreateUiOsh),
    path('PersonUIOsh/<id>/delete/', views.mgdeleteUIOsh ),
    path('PersonUIOsh/<id>/update/', views.mgupdateUIOsh),
    # 
    path('PersonBCBi/create/', views.mgcreateBcBi),
    path('PersonBCBi/<id>/delete/', views.mgdeleteBcBi ),
    path('PersonBCBi/<id>/update/', views.mgupdateBcBi),
    path('PersonFronBi/create/', views.mgcreateFronBi),
    path('PersonFronBi/<id>/delete/', views.mgdeleteFronBi ),
    path('PersonFronBi/<id>/update/', views.mgupdateFronBi),
    path('PersonFullBi/create/', views.mgcreateFullBi),
    path('PersonFullBi/<id>/delete/', views.mgdeleteFullBi ),
    path('PersonFullBi/<id>/update/', views.mgupdateFullBi),
    path('PersonUIBi/create/', views.mgcreateUIBi),
    path('PersonUIBi/<id>/delete/', views.mgdeleteUIBi ),
    path('PersonUIBi/<id>/update/', views.mgupdateUIBi),
    # 
    path('PersonBCUz/create/', views.mgcreateBcUz),
    path('PersonBCUz/<id>/delete/', views.mgdeleteBcUz ),
    path('PersonBCUz/<id>/update/', views.mgupdateBcUz),
    path('PersonFronUz/create/', views.mgcreateFronUz),
    path('PersonFronUz/<id>/delete/', views.mgdeleteFronUz ),
    path('PersonFronUz/<id>/update/', views.mgupdateFronUz),
    path('PersonFullUz/create/', views.mgcreateFullUz),
    path('PersonFullUz/<id>/delete/', views.mgdeleteFullUz ),
    path('PersonFullUz/<id>/update/', views.mgupdateFullUz),
    path('PersonUIUz/create/', views.mgcreateUIUz),
    path('PersonUIUz/<id>/delete/', views.mgdeleteUIUz ),
    path('PersonUIUz/<id>/update/', views.mgupdateUIUz),
    #
    # 
    path('EvPersonBCOsh/create/', views.evcreateBcOsh),
    path('EvPersonBCOsh/<id>/delete/', views.evdeleteBcOsh ),
    path('EvPersonBCOsh/<id>/update/', views.evupdateBcOsh),
    path('EvPersonFronOsh/create/', views.evcreateFronOsh),
    path('EvPersonFronOsh/<id>/delete/', views.evdeleteFronOsh ),
    path('EvPersonFronOsh/<id>/update/', views.evupdateFronOsh),
    path('EvPersonFullOsh/create/', views.evcreateFullOsh),
    path('EvPersonFullOsh/<id>/delete/', views.evdeleteFullOsh ),
    path('EvPersonFullOsh/<id>/update/', views.evupdateFullOsh),
    path('EvPersonUIOsh/create/', views.evcreateUIOsh),
    path('EvPersonUIOsh/<id>/delete/', views.evdeleteUIOsh ),
    path('EvPersonUIOsh/<id>/update/', views.evupdateUIOsh),
    # 
    path('EvPersonBCBi/create/', views.evcreateBcBi),
    path('EvPersonBCBi/<id>/delete/', views.evdeleteBcBi ),
    path('EvPersonBCBi/<id>/update/', views.evupdateBcBi),
    path('EvPersonFronBi/create/', views.evcreateFronBi),
    path('EvPersonFronBi/<id>/delete/', views.evdeleteFronBi ),
    path('EvPersonFronBi/<id>/update/', views.evupdateFronBi),
    path('EvPersonFullBi/create/', views.evcreateFullBi),
    path('EvPersonFullBi/<id>/delete/', views.evdeleteFullBi ),
    path('EvPersonFullBi/<id>/update/', views.evupdateFullBi),
    path('EvPersonUIBi/create/', views.evcreateUIBi),
    path('EvPersonUIBi/<id>/delete/', views.evdeleteUIBi ),
    path('EvPersonUIBi/<id>/update/', views.evupdateUIBi),
    # 
    path('EvPersonBCUz/create/', views.evcreateBcUz),
    path('EvPersonBCUz/<id>/delete/', views.evdeleteBcUz ),
    path('EvPersonBCUz/<id>/update/', views.evupdateBcUz),
    path('EvPersonFronUz/create/', views.evcreateFronUz),
    path('EvPersonFronUz/<id>/delete/', views.evdeleteFronUz ),
    path('EvPersonFronUz/<id>/update/', views.evupdateFronUz),
    path('EvPersonFullUz/create/', views.evcreateFullUz),
    path('EvPersonFullUz/<id>/delete/', views.evdeleteFullUz ),
    path('EvPersonFullUz/<id>/update/', views.evupdateFullUz),
    path('EvPersonUIUz/create/', views.evcreateUIUz),
    path('EvPersonUIUz/<id>/delete/', views.evdeleteUIUz ),
    path('EvPersonUIUz/<id>/update/', views.evupdateUIUz),
    #
]