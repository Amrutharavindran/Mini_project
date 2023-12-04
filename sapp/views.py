from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from datetime import datetime


from sapp.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

def  home(request):
    return render(request,"homeindex.html")

def login(request):
    return render(request,'login index.html')


def logout(request):
    auth.logout(request)
    return render(request,'login index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def logincode(request):

    username=request.POST['textfield']
    password=request.POST['textfield2']


    try:
        ob = login_table.objects.get(Username=username, Password=password)
        if ob.type == 'admin':
            ob1=auth.authenticate(username="123",password="123")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid']=ob.id
            return HttpResponse('''<script>; window.location="/ahome"</script>''')
        elif ob.type=='user':
            ob1 = auth.authenticate(username="123", password="123")
            if ob1 is not None:
                auth.login(request, ob1)
                request.session['lid'] = ob.id
            request.session['lid']=ob.id
            return HttpResponse('''<script>; window.location="/userhome"</script>''')
        elif ob.type=='agent':
            ob1 = auth.authenticate(username="123", password="123")
            if ob1 is not None:
                auth.login(request, ob1)
                request.session['lid'] = ob.id
            request.session['lid'] = ob.id
            return HttpResponse('''<script>; window.location="/aghome"</script>''')
        else:
         return HttpResponse('''<script>alert("Invalid");window.location='/' </script>''')
    except:
         return HttpResponse('''<script>alert("Invalid username and password");window.location='/login' </script>''')


@login_required(login_url='/')
def ahome(request):
    return render(request,'Admin/Admin homepage.html')

@login_required(login_url='/')
def addag(request):
    return render(request, 'Admin/Add Agent.html')

@login_required(login_url='/')
def addagentpost(request):
    name=request.POST['textfield']
    Date_Of_Birth=request.POST['textfield2']
    image=request.FILES['image']
    fs = FileSystemStorage()
    fsave = fs.save(image.name, image)
    place=request.POST['textfield3']
    post=request.POST['textfield4']
    pin=request.POST['textfield5']
    email=request.POST['textfield6']
    phoneNo=request.POST['textfield7']
    username = request.POST['textfield8']
    password = request.POST['textfield9']

    ob=login_table()
    ob.Username=username
    ob.Password=password
    ob.type='agent'
    ob.save()
    ab=Agent_table()
    ab.Name=name
    ab.Dob=Date_Of_Birth
    ab.Photo=fsave
    ab.Place=place
    ab.Post=post
    ab.Pin=pin
    ab.Email=email
    ab.Phone=phoneNo
    ab.LOGIN = ob
    ab.save()
    return HttpResponse('''<script>alert("New agent added"); window.location="/manage_agent"</script>''')
@login_required(login_url='/')
def dltag(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted successfully"); window.location="/manage_agent"</script>''')

@login_required(login_url='/')
def editag(request,id):
    ob=Agent_table.objects.get(id=id)
    request.session['aid']=id
    return render(request, 'Admin/editagent.html',{"i":ob,"d":str(ob.Dob)})

@login_required(login_url='/')
def editagpost(request):
    if "image" in request.FILES:
        name=request.POST['textfield']
        Date_Of_Birth=request.POST['textfield2']
        image=request.FILES['image']
        fs = FileSystemStorage()
        fsave = fs.save(image.name, image)
        place=request.POST['textfield3']
        post=request.POST['textfield4']
        pin=request.POST['textfield5']
        email=request.POST['textfield6']
        phoneNo=request.POST['textfield7']

        ab = Agent_table.objects.get(id=request.session['aid'])
        ab.Name = name
        ab.Dob = Date_Of_Birth
        ab.Photo = fsave
        ab.Place = place
        ab.Post = post
        ab.Pin = pin
        ab.Email = email
        ab.Phone = phoneNo
        ab.save()
        return HttpResponse('''<script>alert("Edited successfully"); window.location="/manage_agent"</script>''')
    else:
        name = request.POST['textfield']
        Date_Of_Birth = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        email = request.POST['textfield6']
        phoneNo = request.POST['textfield7']
        ab = Agent_table.objects.get(id=request.session['aid'])
        ab.Name = name
        ab.Dob = Date_Of_Birth
        ab.Place = place
        ab.Post = post
        ab.Pin = pin
        ab.Email = email
        ab.Phone = phoneNo
        ab.save()
        return HttpResponse('''<script>alert("Edited successfully"); window.location="/manage_agent"</script>''')

def search_ag(request):
    Name=request.POST['textfield']
    ob=Agent_table.objects.filter(Name__contains=Name)
    return render(request,'Admin/Manage agent.html',{'val':ob})
@login_required(login_url='/')
def managepol(request):
    ob = Policy_table.objects.all().order_by('-id')
    print(ob,"================")
#     return render(request, 'Admin/Manage policy.html',{'val':ob})
#
# def my_view(request):
    my_objects = Policy_table.objects.all().order_by('-id')

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    # Pass the Page object to the template
    return render(request, 'Admin/Manage policy.html',  {'my_objects': my_objects})
    # return render(request, 'your_template.html', {'my_objects': my_objects})




@login_required(login_url='/')
def viewpremium(request,id):
    ob=Premium_Details_table.objects.filter(POLICY__id=id)
    return render(request,"admin/view primum.html",{'val':ob})

def viewpremium1(request,id):
    ob=Premium_Details_table.objects.filter(POLICY__id=id)
    return render(request,"User/view premium1.html",{'val':ob})
@login_required(login_url='/')
def addpol(request):
    return render(request, 'Admin/Add policy.html')

@login_required(login_url='/')
def ad_polpost(request):
    policyname= request.POST['textfield']
    policydetails= request.POST['textarea']
    # premium=request.POST['textfield1']
    Type= request.POST['type']
    date= datetime.today()

    ap=Policy_table()
    ap.Policyname = policyname
    ap.Policydetails = policydetails
    # ap.premium=premium
    ap.Date = date
    ap.type=Type
    ap.save()
    if Type=="Vehicle":
         return HttpResponse('''<script>alert("Successfully added policy"); window.location="/managepol"</script>''')
    else:
        request.session['pid']=ap.id
        l=[]
        for i in range(2,100):
            l.append(i)
        return render(request,"Admin/Add policy1.html",{"l":l})
@login_required(login_url='/')
def ad_polpostcode(request):
   maxage=request.POST['select2']
   minage=request.POST['select']
   amount=request.POST['textfield2']

   ap=Premium_Details_table()
   ap.minage=minage
   ap.maxage=maxage
   ap.premium_amount=amount
   ap.POLICY=Policy_table.objects.get(id=request.session['pid'])
   ap.save()
   ob=Premium_Details_table.objects.filter(POLICY__id=request.session['pid'])
   lst=request.session['lst']
   print(ob,"=================================")
   return render(request, "Admin/Add policy2.html",{'val':ob,"lst":lst})
@login_required(login_url='/')
def delete_Premium_Details(request,id):


   ap=Premium_Details_table.objects.get(id=id)

   ap.delete()
   ob=Premium_Details_table.objects.filter(POLICY__id=request.session['pid'])
   lst=request.session['lst']
   print(ob,"=================================")
   return render(request, "Admin/Add policy2.html",{'val':ob,"lst":lst})
@login_required(login_url='/')
def ad_polpost1(request):
    minage= request.POST['textfield']
    maxage= request.POST['textfield1']
    Typ= request.POST['textarea']
    dc= request.POST['selecttt']
    al= request.POST['select']+" to "+request.POST['select1']
    ob=Policy_details_table()
    ob.min_age=minage
    ob.max_age=maxage
    ob.Type=Typ
    ob. Dependents_count=dc
    ob.Dependents_agelimit=al
    ob.POLICY = Policy_table.objects.get(id=request.session['pid'])
    ob.save()
    lst=[]
    for i in range(int(minage),int(maxage)+1):
        lst.append(i)
    request.session['lst']=lst
    return render(request,"Admin/Add policy2.html",{"lst":lst})
    # return HttpResponse('''<script>alert("Successfully added policy"); window.location="/managepol"</script>''')



@login_required(login_url='/')
def dltpl(request,id):
    ob=Policy_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Policy deleted"); window.location="/managepol"</script>''')


@login_required(login_url='/')
def editpol(request,id):
    ob=Policy_table.objects.get(id=id)
    request.session['pid']=id
    return render(request, 'Admin/editpolicy.html',{"i":ob,"d":str(ob.Date)})


@login_required(login_url='/')
def editpolipost(request):
        Policyname=request.POST['textfield']
        Policydetails=request.POST['textfield2']
        Date=request.POST['textfield3']

        ab = Policy_table.objects.get(id=request.session['pid'])
        ab.Policyname = Policyname
        ab.Policydetails = Policydetails
        ab.Date= Date
        ab.save()
        return HttpResponse('''<script>alert("Edited successfully"); window.location="/managepol"</script>''')

@login_required(login_url='/')
def edit_fam(request,id):
    ab=family_table.objects.get(id=id)
    request.session['fid']=id
    print(ab.relation)
    return render(request,'User/edit_fam.html',{"val":ab,"d":str(ab.dob),"r":str(ab.relation)})

@login_required(login_url='/')
def edit_family(request):
    print(request.POST)
    if 'image' in request.FILES:
        Name=request.POST['textfield']
        Dob=request.POST['textfield1']
        Address=request.POST['textfield2']
        Gender=request.POST['radiobutton']
        Id =request.FILES['image']
        fs = FileSystemStorage()
        fsave = fs.save(Id.name,Id)
        Relation=request.POST['select']
        ab=family_table.objects.get(id=request.session['fid'])
        ab.name=Name
        ab.dob=Dob
        ab.address=Address
        ab.id_proof=fsave
        ab.gender=Gender
        ab.relation=Relation
        ab.save()
    else:
        Name=request.POST['textfield']
        Dob=request.POST['textfield1']
        Address=request.POST['textfield2']
        Gender=request.POST['radiobutton']
        Relation=request.POST['select']
        ab=family_table.objects.get(id=request.session['fid'])
        ab.name=Name
        ab.dob=Dob
        ab.address=Address
        ab.gender=Gender
        ab.relation=Relation
        ab.save()

    obp = Policy_details_table.objects.get(POLICY__id=request.session['pid'])
    print("===========================")
    print(obp.Dependents_count)

    # return HttpResponse('''<script>alert("send successfully"); window.location="/sndpolreq"</script>''')
    # else:

    ob = family_table.objects.filter(REQUEST__id=request.session['rid'])
    s = "1"
    if int(obp.Dependents_count) + 1 == len(ob):
        s = "2"
    print(s, "+++++++++++++++++++++++++==================")
    return render(request, "User/view family details.html", {"val": ob, "s": s})
@login_required(login_url='/')
def delete_fam(request,id):
    ab=family_table.objects.get(id=id)
    ab.delete()
    obp = Policy_details_table.objects.get(POLICY__id=request.session['pid'])
    print("===========================")
    print(obp.Dependents_count)


    ob = family_table.objects.filter(REQUEST__id=request.session['rid'])
    s = "1"
    if int(obp.Dependents_count) + 1 == len(ob):
        s = "2"
    print(s, "+++++++++++++++++++++++++==================")
    return render(request, "User/view family details.html", {"val": ob, "s": s})

@login_required(login_url='/')
def search_pol(request):
    Policyname=request.POST['textfield']
    my_objects=Policy_table.objects.filter(Policyname__contains=Policyname)

    # my_objects = Policy_table.objects.all().order_by('-id')

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request,'Admin/Manage policy.html',{'my_objects':my_objects})

@login_required(login_url='/')
def assign(request,id):
    request.session['rid']=id
    ob = Agent_table.objects.all()
    return render(request, 'Admin/Assign request to agent.html',{'val':ob})
@login_required(login_url='/')
def assign1(request):
    rid=request.session['rid']
    aid=request.POST['select']
    obr=Request_table.objects.get(id=rid)
    obr.Status="Assigned"
    obr.save()
    ob=Assign_table()
    ob.Date=datetime.today()
    ob.Status="Assigned"
    ob.AGENT=Agent_table.objects.get(id=aid)
    ob.REQUEST=obr
    ob.save()
    return HttpResponse('''<script>alert("Allocated"); window.location="/viewpolreq"</script>''')


@login_required(login_url='/')
def manage_agent(request):
    ob = Agent_table.objects.all().order_by('-id')
    return render(request,'Admin/Manage agent.html',{'val':ob})

# def managepol(request):
#     ob = Policy_table.objects.all()
#     return render(request, 'Admin/Manage policy.html',{'val':ob})
@login_required(login_url='/')
def reply(request,id):
    ob=Complaint_table.objects.get(id=id)
    request.session['comid']=id
    return render(request, 'Admin/send reply.html',{'val':ob})



@login_required(login_url='/')
def sendrepplyyy(request):
    r=request.POST['textarea']
    ob=Complaint_table.objects.get(id=request.session['comid'])
    ob.Reply=r
    ob.save()
    return HttpResponse('''<script>alert("send successfully"); window.location="/viewcomp"</script>''')

@login_required(login_url='/')
def verify(request):
    ob=Claim_request_table.objects.all().order_by('-id')
    return render(request, 'Admin/View and verify claim.html',{'val':ob})
@login_required(login_url='/')
def Accept_claim(request,id):
    ob = Claim_request_table.objects.get(id=id)
    ob.status="accept"
    ob.save()
    return HttpResponse('''<script>alert("Accepted successfully"); window.location="/verify"</script>''')
@login_required(login_url='/')
def Reject_claim(request,id):
    ob = Claim_request_table.objects.get(id=id)
    ob.status="reject"
    ob.save()
    return HttpResponse('''<script>alert("Rejected "); window.location="/verify"</script>''')


@login_required(login_url='/')
def viewcomp(request):
    ob = Complaint_table.objects.all().order_by('-id')
    return render(request, 'Admin/view complaint.html',{'val':ob})
@login_required(login_url='/')
def search_comp(request):
    Date=request.POST['textfield']
    ob=Complaint_table.objects.filter(Date=Date)
    return render(request,'Admin/view complaint.html',{'val':ob,"d":Date})


@login_required(login_url='/')
def viewfeed(request):
    ob = Feedback_table.objects.all()
    return render(request, 'Admin/view feedback and rating.html',{'val':ob})
@login_required(login_url='/')
def search_feed(request):
    Date=request.POST['textfield']
    ob=Feedback_table.objects.filter(Date=Date)
    return render(request,'Admin/view feedback and rating.html',{'val':ob,"d":Date})


@login_required(login_url='/')
def viewpay(request):
    ob=payment_table.objects.all().order_by('-id')
    return render(request, 'Admin/view payment details.html',{'val':ob})


@login_required(login_url='/')
def search_pay(request):
    Date=request.POST['textfield']
    ob=payment_table.objects.filter(Date=Date)
    return render(request,'Admin/view payment details.html',{'val':ob,"d":Date})

@login_required(login_url='/')
def viewpolreq(request):
    ob = Request_table.objects.all().order_by('-id')
    return render(request, 'Admin/View request for policy.html',{'val':ob})
@login_required(login_url='/')
def view_family(request,id):
    ob=family_table.objects.filter(REQUEST__id=id)
    request.session['reqid']=id
    return render(request, 'Admin/view family.html',{'val':ob})
@login_required(login_url='/')
def view_vehicle(request,id):
    ob=vehicle_table.objects.filter(REQUEST__id=id)
    request.session['vid']=id
    return render(request,'Admin/view vehicle.html',{'val':ob})
@login_required(login_url='/')
def accept_vehicle(request,id):
    ob2=Request_table.objects.get(id=id)
    ob2.Status="accept"
    ob2.save()
    return HttpResponse('''<script>alert("Accepted successfully"); window.location="/viewpolreq"</script>''')

@login_required(login_url='/')
def reject_vehicle(request,id):
    ob2 = Request_table.objects.get(id=id)
    ob2.Status = "reject"
    ob2.save()
    return HttpResponse('''<script>alert("Rejected successfully"); window.location="/viewpolreq"</script>''')

@login_required(login_url='/')
def Accept_request(request):
    ob1=family_table.objects.filter(REQUEST__id=request.session['reqid'])
    for i in ob1:
        ob = Request_table.objects.get(id=i.REQUEST.id)
        ob.Status="accept"
        ob.save()
        return HttpResponse('''<script>alert("Accepted successfully"); window.location="/viewpolreq"</script>''')
@login_required(login_url='/')
def Reject_request(request):
    ob1 = family_table.objects.filter(REQUEST__id=request.session['reqid'])
    for i in ob1:
        ob = Request_table.objects.get(id=i.REQUEST.id)
        ob.Status="reject"
        ob.save()
        return HttpResponse('''<script>alert("Rejected successfully"); window.location="/viewpolreq"</script>''')
@login_required(login_url='/')
def apply(request,id):
    print(request.POST)
    uob=User_table.objects.get(LOGIN__id=request.session['lid'])
    obp=Policy_table.objects.get(id=id)
    print(obp.type,id)
    ob = Request_table()
    ob.POLICY=obp
    ob.Status="processing"
    ob.USERID=User_table.objects.get(LOGIN__id=request.session['lid'])
    ob.Date=datetime.today()
    ob.save()
    request.session['rid']=ob.id
    request.session['pid']=id
    if obp.type=="Health":
        obb = Policy_details_table.objects.get(POLICY__id=id)
        mi = int(obb.min_age)
        ma = int(obb.max_age)
        y = int(datetime.now().strftime("%Y"))
        bd = datetime.now().strftime("-%m-%d")
        md = str(y - ma) + bd
        mm = str(y - mi) + bd
        return render(request,"User/send family request1.html",{"min":md,"max":mm,'v':uob})
    else:
        return render(request,"User/send vehicle request.html")
    return HttpResponse('''<script>alert("Applied successfully"); window.location="/sndpolreq"</script>''')
@login_required(login_url='/')
def send_fam_details(request):
    return render(request,'User/send family request.html')
@login_required(login_url='/')
def applypost(request):
    print(request.POST)

    # name=request.POST["textfield1"]
    # dob=request.POST["textfield2"]
    # gender=request.POST["radiobutton"]
    # address=request.POST["textfield3"]
    uob=User_table.objects.get(LOGIN__id=request.session['lid'])

    image=request.FILES["image"]
    fs = FileSystemStorage()
    fsave = fs.save(image.name, image)
    relation=request.POST["select"]

    ob=family_table()
    ob.name=uob.Firstname+" "+uob.Lastname
    ob.dob=uob.Dob
    ob.gender=uob.Gender
    ob.address=uob.Place+","+uob.Post
    ob.relation=relation
    ob.id_proof=fsave
    ob.REQUEST=Request_table.objects.get(id=request.session['rid'])
    ob.save()
    obp = Policy_details_table.objects.get(POLICY__id=request.session['pid'])
    print("===========================")
    print(obp.Dependents_count)
    if str(obp.Dependents_count) == "0":
        ob=Request_table.objects.get(id=request.session['rid'])
        ob.Status="pending"
        ob.save()
        return HttpResponse('''<script>alert("send successfully"); window.location="/sndpolreq"</script>''')
    else:
        ob=family_table.objects.filter(REQUEST__id=request.session['rid'])
        return render(request, "User/view family details.html",{"val":ob})

@login_required(login_url='/')
def complete_request(request):
    ob = Request_table.objects.get(id=request.session['rid'])
    ob.Status = "pending"
    ob.save()
    return HttpResponse('''<script>alert("send successfully"); window.location="/sndpolreq"</script>''')
def applypost1(request):

    name=request.POST["textfield"]
    dob=request.POST["textfield1"]
    gender=request.POST["radiobutton"]
    # address=request.POST["textfield2"]
    uob=User_table.objects.get(LOGIN__id=request.session['lid'])

    image=request.FILES["image"]
    fs = FileSystemStorage()
    fsave = fs.save(image.name, image)
    relation=request.POST["select"]

    ob=family_table()
    ob.name=name
    ob.dob=dob
    ob.gender=gender
    ob.address = uob.Place + "," + uob.Post
    ob.relation=relation
    ob.id_proof=fsave
    ob.REQUEST=Request_table.objects.get(id=request.session['rid'])
    ob.save()
    obp = Policy_details_table.objects.get(POLICY__id=request.session['pid'])
    print("===========================")
    print(obp.Dependents_count)

        # return HttpResponse('''<script>alert("send successfully"); window.location="/sndpolreq"</script>''')
    # else:

    ob=family_table.objects.filter(REQUEST__id=request.session['rid'])
    s="1"
    if int(obp.Dependents_count)+1==len(ob):
        s="2"
    print(s,"+++++++++++++++++++++++++==================")
    return render(request, "User/view family details.html",{"val":ob,"s":s})



@login_required(login_url='/')
def vehicleapply(request):
    print(request.POST)
    try:
        print(request.session['rid'], "===============")
        print(request.session['pid'], "+++++++++++++++")
        type=request.POST["select"]
        number=request.POST["textfield"]
        image=request.FILES["image"]
        fs=FileSystemStorage()
        fsave=fs.save(image.name,image)

        ob = Request_table.objects.get(id=request.session['rid'])
        ob.Status = "pending"
        ob.save()

        ap=vehicle_table()
        ap.vehicle_type=type
        ap.vehicle_no=number
        ap.rcbook=fsave
        ap.REQUEST =Request_table.objects.get(id=request.session['rid'])
        ap.save()
        return HttpResponse('''<script>alert("send successfully"); window.location="/sndpolreq"</script>''')
    except Exception as e:
        print(e)
@login_required(login_url='/')
def viewwork(request):
    ob = Assign_table.objects.all().order_by('-id')
    return render(request, 'Admin/View Work Status.html',{'val':ob})
@login_required(login_url='/')
def addclm(request,id):
    request.session['cid']=id
    return render(request, 'Agent/Add Claim.html')
@login_required(login_url='/')
def addclmpost(request):
    ClaimAmount=request.POST['textfield']
    Date=request.POST['textfield2']
    image=request.FILES['image']
    fs = FileSystemStorage()
    fsave = fs.save(image.name, image)
    ap = Claim_table()
    ap.claimamount = ClaimAmount
    ap.Date=Date
    ap.Photo= fsave
    ap.CLAIM_REQ=Claim_request_table.objects.get(id=request.session['cid'])
    ap.save()
    return HttpResponse('''<script>alert("Claim added succesfully"); window.location="/manageclm"</script>''')


def aghome(request):
    return render(request,'Agent/Agent homepage.html')
@login_required(login_url='/')
def chat(request):
    return render(request, 'Agent/Chat with user.html')
@login_required(login_url='/')
def manageclm(request):
    ob = Claim_request_table.objects.filter(status='accepted',ASSIGN__AGENT__LOGIN__id=request.session['lid'])
    print(ob)
    print("++++++++++++++++++++=============================")
    for i in ob:
        print(i)
        print(i.ASSIGN.REQUEST.POLICY.Policyname)
    return render(request, 'Agent/Manage Claim.html',{'val': ob})
@login_required(login_url='/')
def updatewrk(request):
    return render(request, 'Agent/update work status.html')
@login_required(login_url='/')
def viewassign(request):

    ob=Assign_table.objects.filter(AGENT__LOGIN__id=request.session['lid'])
    return render(request, 'Agent/View assigned work.html',{'val':ob})
@login_required(login_url='/')
def updatestatus(request,id):
    request.session['aid']=id

    return render(request, 'Agent/update work status.html')
@login_required(login_url='/')
def updatestatus1(request):
    id=request.session['aid']
    sta=request.POST['textarea']
    ob=Assign_table.objects.get(id=id)
    ob.Status=sta
    ob.save()
    return HttpResponse('''<script>alert("Updated successfully"); window.location="/viewassign"</script>''')

@login_required(login_url='/')
def payment_view(request):
    ob1=Assign_table.objects.filter(AGENT__LOGIN=request.session['lid'])
    lst=[]
    for i in ob1:
        obb = payment_table.objects.filter(POLICY__id=i.REQUEST.POLICY.id)
        for k in obb:
            lst.append(k.id)
    ob=payment_table.objects.filter(id__in=lst).order_by('-id')
    return render(request, 'Agent/view payment details.html',{'val': ob})

@login_required(login_url='/')
def sndpolreq(request):
    ob=Request_table.objects.filter(Status='processing')
    for i in ob:
        i.delete()
    ob= Policy_table.objects.all()

    print(ob, "================")
    #     return render(request, 'Admin/Manage policy.html',{'val':ob})
    #
    # def my_view(request):
    my_objects =Policy_table.objects.all().order_by('-id')
    print(my_objects,"**********************************")
    print(my_objects,"**********************************")
    print(my_objects,"**********************************")
    print(my_objects,"**********************************")

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request,'User/send request for policy.html',{'my_objects':my_objects})

@login_required(login_url='/')
def viewpoldetails(request,id):
    ob=Policy_details_table.objects.filter(POLICY__id=id)
    return render(request,'User/viewpoldetails.html',{'val':ob})
@login_required(login_url='/')
def viewpoldetail(request,id):
    ob = Policy_details_table.objects.filter(POLICY__id=id)
    return render(request,'Admin/viewpoldetail.html',{'val':ob})

@login_required(login_url='/')
def search_poly(request):
    Policyname=request.POST['t1']
    ptype=request.POST['t2']
    pamt=request.POST['t3']
    if Policyname != "":
        ob=Policy_table.objects.filter(Policyname__icontains=Policyname)
        my_objects =ob
        print(my_objects, "**********************************")
        print(my_objects, "**********************************")
        print(my_objects, "**********************************")
        print(my_objects, "**********************************")

        # Set the number of items per page
        items_per_page = 5

        # Create a Paginator instance
        paginator = Paginator(my_objects, items_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request,'User/send request for policy.html',{'my_objects':my_objects})
    elif ptype != "":
        ob = Policy_table.objects.filter(type__icontains=ptype)
        my_objects = ob

        items_per_page = 5

        # Create a Paginator instance
        paginator = Paginator(my_objects, items_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request, 'User/send request for policy.html', {'my_objects': my_objects})
    elif pamt != "":
        ob = Policy_table.objects.filter(Date=pamt)
        my_objects = ob

        items_per_page = 5

        # Create a Paginator instance
        paginator = Paginator(my_objects, items_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request, 'User/send request for policy.html', {'my_objects': my_objects})
    else:
        if pamt != "":
            ob = Policy_table.objects.filter(premium__lte=pamt,type__icontains=ptype,Policyname__icontains=Policyname)
            my_objects = ob

            items_per_page = 5

            # Create a Paginator instance
            paginator = Paginator(my_objects, items_per_page)

            # Get the current page number from the request's GET parameters
            page = request.GET.get('page')

            try:
                # Get the Page object for the requested page
                my_objects = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver the first page
                my_objects = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g., 9999), deliver the last page
                my_objects = paginator.page(paginator.num_pages)

            return render(request, 'User/send request for policy.html', {'my_objects': my_objects})

        else:
            ob = Policy_table.objects.filter( type__icontains=ptype,Policyname__icontains=Policyname)
            my_objects = ob

            items_per_page = 5

            # Create a Paginator instance
            paginator = Paginator(my_objects, items_per_page)

            # Get the current page number from the request's GET parameters
            page = request.GET.get('page')

            try:
                # Get the Page object for the requested page
                my_objects = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver the first page
                my_objects = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g., 9999), deliver the last page
                my_objects = paginator.page(paginator.num_pages)

            return render(request, 'User/send request for policy.html', {'my_objects': my_objects})


def pay(request):
    ob=payment_table.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'User/payment.html',{'val':ob})


@login_required(login_url='/')

def payment(request):
    obj=Request_table.objects.filter(USERID__LOGIN__id=request.session['lid'],Status='Assigned')
    ob = User_table.objects.get(LOGIN__id=request.session['lid'])
    today = datetime.today()
    age = today.year - ob.Dob.year - ((today.month,today.day) < (ob.Dob.month, ob.Dob.day))
    print(age, 'jjjjjjjjjjjjj')
    return render(request, 'User/pay.html',{'val':obj})




@login_required(login_url='/')
def clmreq(request):
    obj=Assign_table.objects.filter(REQUEST__USERID__LOGIN__id=request.session['lid'],REQUEST__Status='Assigned')
    return render(request, 'User/send claim request with documents.html',{'val':obj})

@login_required(login_url='/')

def sendclm(request):
    assignid=request.POST['policy']
    reason=request.POST['textarea']
    date = datetime.today()
    documents=request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(documents.name, documents)

    ab=Claim_request_table()
    ab.Reason=reason
    ab.ASSIGN=Assign_table.objects.get(id=assignid)
    ab.Documents=fsave
    ab.Date=date
    ab.status='pending'
    ab.save()
    return HttpResponse('''<script>alert("send successfully"); window.location="/clmreq"</script>''')


def viewrply(request):
    ob=Complaint_table.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'User/Send complaint and view reply.html',{'val':ob})

@login_required(login_url='/')
def sndcomp(request):
    return render(request, 'User/send complaint.html',)

@login_required(login_url='/')
def sendcompl(request):
    comp=request.POST['textarea']

    ab=Complaint_table()
    ab.Complaint=comp
    ab.Reply='pending'
    ab.Date=datetime.today()
    ab.USER=User_table.objects.get(LOGIN__id=request.session['lid'])
    ab.save()
    return HttpResponse('''<script>alert("send successfully"); window.location="/viewrply"</script>''')










def sndfeed(request):
   return render(request,'User/send feedback and rating.html')

def sendfeed(request):
    feed=request.POST['textarea']
    rating=request.POST['select']

    ab=Feedback_table()
    ab.Feedback=feed
    ab.Rating=rating
    ab.Date=datetime.today()
    ab.USER=User_table.objects.get(LOGIN__id=request.session['lid'])
    ab.save()
    return HttpResponse('''<script>alert("send successfully"); window.location="/userhome"</script>''')

@login_required(login_url='/')
def userhome(request):
    return render(request, 'user_index.html')
@login_required(login_url='/')
def clmstatus(request):
    ob=Claim_request_table.objects.filter(ASSIGN__REQUEST__USERID__LOGIN__id=request.session['lid'])
    return render(request, 'User/View Claim request status.html',{'val':ob})
@login_required(login_url='/')
def reqstatus(request):
    print(request.session['lid'],"vvvvvvvvvvvv")
    ob=Request_table.objects.filter(USERID__LOGIN__id=request.session['lid'])
    for i in ob:
        if i.Status=="Assigned":
            ob1=Assign_table.objects.get(REQUEST__id=i.id)
            i.name=ob1.AGENT.Name
    return render(request, 'User/view request status.html',{'val':ob})

def ureg(request):
    return render(request, 'register index.html')

def uncheck(request):
    un=request.GET['un']
    data = {
        'is_taken': login_table.objects.filter(Username__iexact=un).exists()
    }
    if data['is_taken']:
        data['error_message']="A user with this username already exists."
        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)

def user_reg(request):
    fname=request.POST['textfield']
    lname = request.POST['textfield2']
    gen = request.POST['gender']
    dob =request.POST['textfield3']
    img=request.FILES['file']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    email=request.POST['textfield7']
    phone=request.POST['textfield8']
    unm=request.POST['textfield9']
    pswd=request.POST['textfield10']

    ob=login_table()
    ob.Username=unm
    ob.Password=pswd
    ob.type="user"
    ob.save()

    obu=User_table()
    obu.Firstname=fname
    obu.Lastname=lname
    obu.Gender=gen
    obu.Dob=dob
    obu.Photo=img
    obu.Place=place
    obu.Post=post
    obu.Pin=pin
    obu.Email=email
    obu.Phone=phone
    obu.LOGIN=ob
    obu.save()
    return HttpResponse('''<script>alert('registered');window.location='/login'</script>''')

def index(request):
    print(request.POST)
    id=request.POST['brand']
    print(id,"=======")
    ob=Request_table.objects.get(id=id)
    request.session['rid']=ob.id
    pid=ob.POLICY.id


    ob = User_table.objects.get(LOGIN__id=request.session['lid'])
    today = datetime.today()
    age = today.year - ob.Dob.year
    obf=family_table.objects.filter(REQUEST__id=id)
    for i in obf:
        age1 = today.year - i.dob.year
        if age1>age:
            age=age1


    print(age, 'jjjjjjjjjjjjj')
    obp = Premium_Details_table.objects.get(POLICY__id=pid,minage__lte=str(age),maxage__gt=age )
    print("=================================")
    return JsonResponse({"task":obp.premium_amount})

def user_pay_proceed( request):
    import razorpay
    amount = request.POST['textfield']
    request.session['pay_amount'] = amount

    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': amount+"00", 'currency': "INR", 'payment_capture': '1'})
    ob=User_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'User/UserPayProceed.html', {"p":payment,"val":ob,"pid":request.session['rid'],"amt":request.session['pay_amount'],"lid":request.session['lid']})

def on_payment_success(request):
    # pid = {{pid}} & amt = {{amt}} & lid = {{lid}}
    amt = request.GET['amt']
    pid= request.GET['pid']
    request.session['lid']=request.GET['lid']
    print(request.GET)
    ob=payment_table()
    obr=Request_table.objects.get(id=pid)
    ob.Date=datetime.today()
    ob.POLICY=Policy_table.objects.get(id=obr.POLICY.id)
    ob.USER=User_table.objects.get(LOGIN=request.session['lid'])
    ob.Amount=amt
    ob.save()
    return HttpResponse('''<script>;window.location="/userhome"</script>''')


"=========================chat withn user=========="
def chatwithuser(request):
    obb=Assign_table.objects.filter(AGENT__LOGIN__id=request.session['lid'])
    if len(obb)==0:
        return HttpResponse(
            '''<script>alert("No assigned users");window.location="/aghome"</script>''')
    else:
        print(obb)
        list=[]
        for i in obb:
            ob1 = User_table.objects.filter(id=i.REQUEST.USERID.id)
            print('ggggggggggggggggggg',ob1)
            for k in ob1:
                list.append(k.id)
        obbb=User_table.objects.filter(id__in=list).distinct()
        print(obbb)
        for p in obbb:
            w=User_table.objects.filter(id=p.id)
    return render(request,"Agent/fur_chat.html",{'val':w})

def chatview(request):
    obb = Assign_table.objects.filter(AGENT__LOGIN__id=request.session['lid'])
    list=[]
    for i in obb:
        ob1 = User_table.objects.filter(id=i.REQUEST.USERID.id)
        for k in ob1:
            list.append(k.id)
    d=[]
    obbb=User_table.objects.filter(id__in=list)
    for i in obbb:
        r={"name":i.Firstname,'photo':i.Photo.url,'email':i.Email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=Chat_table()
    ob.FromID=login_table.objects.get(id=request.session['lid'])
    ob.ToID=login_table.objects.get(id=id)
    ob.Message=msg
    ob.Date=datetime.now().strftime("%Y-%m-%d")
    ob.save()
    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=Chat_table.objects.filter(FromID__id=id,ToID__id=request.session['lid'])
    ob2=Chat_table.objects.filter(FromID__id=request.session['lid'],ToID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FromID.id,"msg":i.Message,"date":i.Date,"chat_id":i.id})
    print(id,"=================================================================")
    print(id,"=================================================================")
    print(id,"=================================================================")
    print(id,"=================================================================")
    obu=Agent_table.objects.get(LOGIN__id=id)
    # obu=User_table.objects.get(LOGIN__id=request.session['lid'])


    return JsonResponse({"data":res,"name":obu.Name,"photo":str(obu.Photo.url),"user_lid":obu.LOGIN.id})


def coun_msg2(request,id):

    ob1=Chat_table.objects.filter(FromID__id=id,ToID__id=request.session['lid'])
    ob2=Chat_table.objects.filter(FromID__id=request.session['lid'],ToID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FromID.id,"msg":i.Message,"date":i.Date,"chat_id":i.id})
    print(id,"=================================================================")
    print(id,"=================================================================")
    print(id,"=================================================================")
    print(id,"=================================================================")
    obu=User_table.objects.get(LOGIN__id=id)
    print(obu)
    # obu=User_table.objects.get(LOGIN__id=request.session['lid'])


    return JsonResponse({"data":res,"name":obu.Firstname+" "+obu.Lastname,"photo":str(obu.Photo.url),"user_lid":obu.LOGIN.id})


def coun_msg1(request,id):

    ob1=Chat_table.objects.filter(FromID__id=id,ToID__id=request.session['lid'])
    ob2=Chat_table.objects.filter(FromID__id=request.session['lid'],ToID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FromID.id,"msg":i.Message,"date":i.Date,"chat_id":i.id})
    print(id,"=================================================================")
    print(id,"=================================================================")
    print(id,"=================================================================")
    print(id,"=================================================================")
    # obu=User_table.objects.get(LOGIN__id=id)
    obu=User_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.Firstname+" "+obu.Lastname,"photo":str(obu.Photo.url),"user_lid":obu.LOGIN.id})


"=========================chat withn agent==============="


def chatwithagent(request):
        obb=Assign_table.objects.filter(REQUEST__USERID__LOGIN__id=request.session['lid'])
        print(request.session['lid'])
        print(obb,"KKKKKKKKKKKKKKK")
        if len(obb)==0:
            return HttpResponse('''<script>alert("No assigned agents");window.location="/userhome"</script>''')
        else:
            print(obb)
            lst=[]
            for i in obb:
                ob2 = Agent_table.objects.filter(id=i.AGENT.id)
                print('ggggggggggggggggggg',ob2)
                for k in ob2:
                   lst.append(k.id)
            #     for k in ob1:
            #         list.append(k.id)
            # obbb=User_table.objects.filter(id__in=list).distinct()
            # print(obbb)
            # for p in obbb:chatwithagent
            #     w=User_table.objects.filter(id=p.id)
            ob1=Agent_table.objects.filter(id__in=lst)
            return render(request,"User/fur_chat with agent.html",{'val':ob1})

def chatviewagent(request):
    obb = Assign_table.objects.filter(REQUEST__USERID__LOGIN__id=request.session['lid'])
    print(obb)
    print(request.session['lid'])
    list=[]
    for i in obb:
        # ob1 = User_table.objects.filter(id=i.AGENT.id)
        # for k in ob1:
        #     list.append(k.id)

            list.append(i.AGENT.id)
    print(list)
    d=[]
    obbb=Agent_table.objects.filter(id__in=list)
    for i in obbb:
        r={"name":i.Name,'photo':i.Photo.url,'email':i.Email,'loginid':i.LOGIN.id}
        d.append(r)
    print(d)
    return JsonResponse(d, safe=False)




def coun_insert_chatagent(request,msg,id):
    print("===",msg,id)
    ob=Chat_table()
    ob.FromID=login_table.objects.get(id=request.session['lid'])
    ob.ToID=login_table.objects.get(id=id)
    ob.Message=msg
    ob.Date=datetime.now().strftime("%Y-%m-%d")
    ob.save()
    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msgagent(request,id):

    ob1=Chat_table.objects.filter(FromID__id=id,ToID__id=request.session['lid'])
    ob2=Chat_table.objects.filter(FromID__id=request.session['lid'],ToID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    print(ob1,"JJJJJJJJJJJJJ")
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FromID.id,"msg":i.Message,"date":i.Date,"chat_id":i.id})

    obu=Agent_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.Name,"photo":str(obu.Photo.url),"user_lid":obu.LOGIN.id})







