from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from authentication.models import user,travel_agency,admin,Verified_travel_agency,schedule
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from os import path
from datetime import datetime
@login_required(login_url='login')
def home(request):
    
    showdata=request.session['um']
    
    if request.method=="POST":
      
        if request.POST.get('form') and request.POST.get('optradio') and request.POST.get('to') and request.POST.get('date') and request.POST.get('time') and request.POST.get('date') and request.POST.get('total_seat')and request.POST.get('date') and request.POST.get('window') and request.POST.get('date') and request.POST.get('general')and request.POST.get('date') and request.POST.get('price')and request.POST.get('date') and request.POST.get('bus_number'):
            saveschedule=schedule()
            st=Verified_travel_agency.objects.get(id=request.session['um'])

            print(request.POST.get('optradio'))
            saveschedule.form=request.POST.get('form')
            saveschedule.date=request.POST.get('date')
            saveschedule.time=request.POST.get('time')
            saveschedule.to=request.POST.get('to')
            saveschedule.bus_number=request.POST.get('bus_number')
            saveschedule.bus_type=request.POST.get('optradio')
            saveschedule.price=request.POST.get('price')
            saveschedule.total_seats=request.POST.get('total_seat')
            saveschedule.window=request.POST.get('window')
            saveschedule.general=request.POST.get('general')
            saveschedule.agency_number=request.session['um']
            saveschedule.agency_name=st.agency_name
            saveschedule.pk=request.session['um']+request.POST.get('bus_number')
            messages.success(request,"schedule successfully added")
            saveschedule.save()
    print(showdata)

    return render(request,'set_schedule.html',{'data':showdata})

@login_required(login_url='adhome')
def adhome(request):
    showem=travel_agency.objects.all()
    return render(request,'fetch_travel_agency_details.html',{'data':showem})
   

def Logoutpage(request):
    logout(request)
    return redirect('login')

def loginpage(request):
     if request.method=="POST":
        uname=request.POST.get('email')
       
        
        pass1=request.POST.get('password')
        users=user.objects.all()
        print(uname)
        print(pass1)
        tv=Verified_travel_agency.objects.all()
        authadmin=admin.objects.all()
        print(authadmin)
        userauth=authenticate(request,username=uname,password=pass1)
        print(userauth)
        if userauth is not None:
            # login(request,userauth)
            # return redirect('home')
            #         print(d.email)
            #         return redirect('check')
              for au in authadmin:
                  if au.mobile_no==uname:
                      login(request,userauth)
                      return redirect('adhome')
              for v in tv:
                  if v.mobile_no==uname:
                      request.session['um']=v.mobile_no
                      print(request.session['um'])
                      login(request,userauth)
                      return redirect('home')
              for s in users:
                      if s.mobile_no==uname:
                          request.session['um']=s.mobile_no
                          login(request,userauth)   
                          return redirect('user_home')
                     # data(request,v.mobile_no)
                     
                      break
        else:
            messages.error(request,"user name or password is worng.if you do not register,then first register and then login")
            return redirect('login')
     return render(request,'login.html')


def history(request):
    showschedule=schedule.objects.all()
    print(datetime.now())
    x=datetime.now()
    v=x.date()
    print(v)
    for d in showschedule:
        if v> d.date:
            d.delete()
        if d.agency_number==request.session['um']:
            mobile=request.session['um']
    print(mobile)
    return render(request,'history.html',{'data':showschedule,'number':mobile})
def signup(request):
    if request.method=="POST":
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
        if request.POST.get('tname') and request.POST.get('phone') and request.POST.get('address') and request.POST.get('aadharno') and request.POST.get('password'):
          if pass1!=pass2:
            messages.warning(request,"your password and confirm password are not same")
            return HttpResponse('signup')
          else:
            saverecord=travel_agency()
            saverecord.agency_name= request.POST.get('tname')
            saverecord.pk=request.POST.get('phone')
            saverecord.mobile_no=request.POST.get('phone')
            saverecord.address=request.POST.get('address')
            saverecord.aadhar_no=request.POST.get('aadharno')
            saverecord.password=request.POST.get('password')
            saverecord.email=request.POST.get('email')
            saverecord.status=False
            saverecord.file="/static/file/"+request.FILES['file'].name
            # print(saverecord.file)
            print(request.FILES)
            handle_uploaded_file(request.FILES['file'])
            my_user=User.objects.create_user(request.POST.get('phone'),request.POST.get('email'),pass1)
            my_user.save()
            saverecord.save()
            messages.success(request,'Travel Agency '+saverecord.agency_name+' is save successfully..!')
            return redirect('login')
        else:
            messages.error(request,'Travel Agency is save successfully..!')
    else:
        return render(request,'registration.html')
    
   
def handle_uploaded_file(f):  
    file_path = path.join(os.getcwd(), "media","file", f.name)
    print(file_path)
    file = open(file_path, 'w+')
    print(f.chunks())
    with open(file_path, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)

def check(request):
    return render(request,"check.html")

def edit(request,id):
    saveschedule=schedule.objects.get(id=id)
    schedule_date=saveschedule.date
    schedule_time=saveschedule.time
    print(schedule_time)
    sh=schedule_time.hour
    smin=schedule_time.minute
    sm=schedule_date.month
    sy=schedule_date.year
    sd=schedule_date.day
    if sm<10:
        sm="0"+str(sm)
    if sd<10:
        sd="0"+str(sd)
    if sh<10:
        sh="0"+str(sh)
    if smin<10:
        smin="0"+str(smin)
    
    schedule_time=saveschedule.time
    print(schedule_date)
    if request.method=="POST":
      
        if request.POST.get('form') and request.POST.get('optradio') and request.POST.get('to') and request.POST.get('date') and request.POST.get('time') and request.POST.get('date') and request.POST.get('total_seat')and request.POST.get('date') and request.POST.get('window') and request.POST.get('date') and request.POST.get('general')and request.POST.get('date') and request.POST.get('price')and request.POST.get('date') and request.POST.get('bus_number'):
            saveschedule=schedule()
            print(request.POST.get('optradio'))
            saveschedule.form=request.POST.get('form')
            saveschedule.date=request.POST.get('date')
            saveschedule.time=request.POST.get('time')
            saveschedule.to=request.POST.get('to')
            saveschedule.bus_number=request.POST.get('bus_number')
            saveschedule.bus_type=request.POST.get('optradio')
            saveschedule.price=request.POST.get('price')
            saveschedule.total_seats=request.POST.get('total_seat')
            saveschedule.window=request.POST.get('window')
            saveschedule.general=request.POST.get('general')
            saveschedule.agency_number=request.session['um']
            saveschedule.pk=request.session['um']+request.POST.get('bus_number')
            messages.success(request,"data successfully edit")
            messages.warning(request,"input data is wrong please check data")
            if messages.success:
                saveschedule.save()
        
            return redirect('history')
    return render(request,'edit.html',{'data':saveschedule,'dd':schedule_date,'m':sm,'y':sy,'d':sd,'tm':schedule_time,'h':sh,'min':smin})

def profile(request):
    id=request.session['um']
    showdata=Verified_travel_agency.objects.get(id=id)
    
    return render(request,'profile.html',{'data':showdata})

def adentry(request):
    if request.method=="POST":
       
      
        if request.POST.get('phone') and request.POST.get('email') and request.POST.get('password'):
         
            saverecord=admin()
            saverecord.pk=request.POST.get('phone')
            saverecord.mobile_no=request.POST.get('phone')
            saverecord.password=request.POST.get('password')
            saverecord.email=request.POST.get('email')
            # print(saverecord.file)
            saverecord.save()
            my_user=User.objects.create_user(request.POST.get('phone'),request.POST.get('email'),request.POST.get('password'))
            my_user.save()
            
            messages.success(request,'admin '+saverecord.mobile_no+' is save successfully..!')
            return redirect('login')
        else:
            
            messages.success(request,'admin is save successfully..!')
           
    else:
        return render(request,'entry.html')

def showemp(request):
    showem=travel_agency.objects.all()
    showvm=Verified_travel_agency.objects.all()
    return render(request,'fetch_travel_agecy_details.html',{'data':showem,'data2':showvm})

def approve(request,id):
    savedata=Verified_travel_agency()
    edit2=travel_agency.objects.get(id=id)
    savedata.agency_name=edit2.agency_name
    savedata.address=edit2.address
    savedata.aadhar_no=edit2.aadhar_no
    savedata.email=edit2.email
    savedata.pk=edit2.pk
    savedata.password=edit2.password
    savedata.mobile_no=edit2.mobile_no
    savedata.file=edit2.file
    savedata.save()
    edit2.status="True"
    edit2.save()
    print(edit2.status)
    messages.success(request,"travel agency successfully approved ")
    return redirect('adhome')

def aprroved(request):
    showem=Verified_travel_agency.objects.all()
    return render(request,'aproved_list.html',{'data':showem})

def dell(request,id):
     edit2=travel_agency.objects.get(id=id)
     User.objects.get(username=id).delete()
     edit2.delete()
     messages.success(request,"travel agency successfully removed ")
     return redirect('adhome')
    # return render(request,"fetch_travel_agency_details.html",{"data1":edit2,'data':showem})

def signup_user(request):
  if request.method=="POST":
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
        if request.POST.get('uname') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('password') and request.POST.get('password1'):
          if pass1!=pass2:
            messages.warning(request,"your password and confirm password are not same")
        
          else:
            saverecord=user()
            saverecord.user_name= request.POST.get('uname')
            saverecord.pk=request.POST.get('phone')
            saverecord.mobile_no=request.POST.get('phone')
            saverecord.password=request.POST.get('password')
            saverecord.email=request.POST.get('email')
            
           
            my_user=User.objects.create_user(request.POST.get('phone'),request.POST.get('email'),pass1)
            my_user.save()
            saverecord.save()
            messages.success(request,saverecord.user_name+' is save successfully..!')
            return redirect('login')
        else:
            messages.error(request,'Travel Agency is save successfully..!')
  else:
        return render(request,'signup_user.html')

def usersu(request):
    return render(request,'home.html')

def user_home(request):
  
   
   if request.method=="POST":
      
        showschedule=schedule.objects.all()
        for s in showschedule:
            if s.date == request.POST.get('date'):
                 sr=s.date
                 break
            

       
        s=request.POST.get('date')
        datetime_str = s

        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date()


        m=datetime_object.strftime("%B")
        dm=datetime_object.day
        d=datetime_object.day
        y=datetime_object.year
       
        dt=datetime_object.strftime(m+' %d, %Y')
        if request.POST.get('form') and request.POST.get('to') and request.POST.get('date'):
            form=request.POST.get('form')
            to=request.POST.get('to')
            date=request.POST.get('date')
            showschedule=schedule.objects.all()
            return render(request,'searched_list.html',{'date':date,'form':form,'to':to,'schedule':showschedule,'dt':dt})
        else:
            
            messages.success(request,'admin is save successfully..!')
   else:
        return render(request,'userhome.html')
    
# Create your views here.
