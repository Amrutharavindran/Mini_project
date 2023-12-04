"""insuranceAgency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from sapp import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('',views.home,name='home'),
    path('user_reg',views.user_reg,name='user_reg'),
    path('ahome',views.ahome,name='ahome'),
    path('addag',views.addag,name='addag'),
    path('addpol',views.addpol,name='addpol'),
    path('assign1',views.assign1,name='assign1'),
    path('assign/<int:id>',views.assign,name='assign'),
    path('manage_agent',views.manage_agent,name='manage_agent'),
    path('managepol',views.managepol,name='managepol'),
    path('reply/<int:id>',views.reply,name='reply'),
    path('sendrepplyyy',views.sendrepplyyy,name='sendrepplyyy'),
    path('verify',views.verify,name='verify'),
    path('viewcomp',views.viewcomp,name='viewcomp'),
    path('viewfeed',views.viewfeed,name='viewfeed'),
    path('viewpay',views.viewpay,name='viewpay'),
    path('viewpolreq',views.viewpolreq,name='viewpolreq'),
    path('viewwork',views.viewwork,name='viewwork'),
    path('addclm/<int:id>',views.addclm,name='addclm'),
    path('aghome',views.aghome,name='aghome'),
    path('chat',views.chat,name='chat'),
    path('manageclm',views.manageclm,name='manageclm'),
    path('updatewrk',views.updatewrk,name='updatewrk'),
    path('viewassign',views.viewassign,name='viewassign'),
    path('payment', views.payment, name='payment'),

    path('pay',views.pay,name='pay'),
    path('clmreq', views.clmreq, name='clmreq'),
    path('sendclm', views.sendclm, name='sendclm'),
    path('viewrply', views.viewrply, name='viewrply'),
    path('sndcomp', views.sndcomp, name='sndcomp'),
    path('sndfeed', views.sndfeed, name='sndfeed'),
    path('userhome', views.userhome, name='userhome'),
    path('clmstatus', views.clmstatus, name='clmstatus'),
    path('reqstatus', views.reqstatus, name='reqstatus'),
    path('ureg', views.ureg, name='ureg'),
    path('logincode', views.logincode, name='logincode'),
    path('ad_polpost',views.ad_polpost, name='ad_polpost'),
    path('ad_polpost1',views.ad_polpost1, name='ad_polpost1'),
    path('addagentpost',views.addagentpost, name='addagentpost'),
    path('editag/<int:id>',views.editag,name='editag'),
    path('dltag/<int:id>',views.dltag,name='dltag'),
    path('editagpost',views.editagpost,name='editagpost'),
    path('editpol/<int:id>',views.editpol,name='editpol'),
    path('accept_vehicle/<int:id>',views.accept_vehicle,name='accept_vehicle'),
    path('reject_vehicle/<int:id>',views.reject_vehicle,name='reject_vehicle'),
    path('dltpl/<int:id>',views.dltpl,name='dltpl'),
    path('uncheck',views.uncheck,name='uncheck'),
    path('Accept_request',views.Accept_request,name='Accept_request'),
    path('Reject_request',views.Reject_request,name='Reject_request'),
    path('editpolipost',views.editpolipost,name='editpolipost'),
    path('Accept_claim/<int:id>',views.Accept_claim,name='Accept_claim'),
    path('Reject_claim/<int:id>',views.Reject_claim,name='Reject_claim'),
    path('search_ag',views.search_ag,name='search_ag'),
    path('search_comp',views.search_comp,name='search_comp'),
    path('search_pol',views.search_pol,name='search_pol'),
    path('search_feed',views.search_feed,name='search_feed'),
    path('search_pay',views.search_pay,name='search_pay'),
    path('updatestatus1',views.updatestatus1,name='updatestatus1'),
    path('updatestatus/<int:id>',views.updatestatus,name='updatestatus'),
    path('apply/<int:id>',views.apply,name='apply'),
    path('addclmpost',views.addclmpost,name='addclmpost'),
    path('sndpolreq',views.sndpolreq,name='sndpolreq'),
    path('search_poly',views.search_poly,name='search_poly'),
    path('sendfeed',views.sendfeed,name='sendfeed'),
    path('payment',views.payment,name='payment'),
    path('payment_view',views.payment_view,name='payment_view'),
    path('sendcompl',views.sendcompl,name='sendcompl'),

    path('pay',views.pay,name='pay'),
    path('index',views.index,name='index'),
    path('user_pay_proceed',views.user_pay_proceed,name='user_pay_proceed'),
    path('on_payment_success',views.on_payment_success,name='on_payment_success'),
    path('applypost',views.applypost,name='applypost'),
    path('applypost1',views.applypost1,name='applypost1'),
    path('send_fam_details',views.send_fam_details,name='send_fam_details'),
    path('vehicleapply',views.vehicleapply,name='vehicleapply'),
    path('complete_request',views.complete_request,name='complete_request'),
    path('view_family/<int:id>',views.view_family,name='view_family'),
    path('view_vehicle/<int:id>', views.view_vehicle, name='view_vehicle'),
    path('delete_fam/<int:id>', views.delete_fam, name='delete_fam'),
    path('edit_fam/<int:id>', views.edit_fam, name='edit_fam'),
    path('edit_family', views.edit_family, name='edit_family'),
    path('viewpoldetails/<int:id>', views.viewpoldetails, name='viewpoldetails'),
    path('viewpoldetail/<int:id>', views.viewpoldetail, name='viewpoldetail'),
    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_msg1/<int:id>', views.coun_msg1, name='coun_msg1'),
    path('coun_msg2/<int:id>', views.coun_msg2, name='coun_msg2'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),
    path('ad_polpostcode',views.ad_polpostcode,name='ad_polpostcode'),

    path('viewpremium/<int:id>',views.viewpremium,name='viewpremium'),
    path('viewpremium1/<int:id>',views.viewpremium1,name='viewpremium1'),



    path('chatwithagent', views.chatwithagent, name='chatwithagent'),
    path('chatviewagent', views.chatviewagent, name='chatviewagent'),
    path('coun_msgagent/<int:id>', views.coun_msgagent, name='coun_msgagent'),
    path('delete_Premium_Details/<int:id>', views.delete_Premium_Details, name='delete_Premium_Details'),
    path('coun_insert_chatagent/<str:msg>/<int:id>', views.coun_insert_chatagent, name='coun_insert_chatagent'),

]
